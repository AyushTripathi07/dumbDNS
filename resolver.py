import uuid
from dnslib import DNSRecord, DNSHeader, RR, QTYPE, TXT
from dnslib.server import DNSServer
from pint import UnitRegistry  # type: ignore

# Initialize unit registry for conversions
ureg = UnitRegistry()

class CustomDNSResolver:
    def resolve(self, request, handler):
        query_name = str(request.q.qname).rstrip(".")
        query_type = QTYPE[request.q.qtype]

        response = DNSRecord(DNSHeader(id=request.header.id, qr=1, aa=1, ra=1), q=request.q)

        try:
            if query_name.endswith(".unit"):
                conversion_query = query_name.split(".")[0]  
                value_unit, target_unit = conversion_query.split("-")
                value = float(value_unit[:-2])  
                source_unit = value_unit[-2:]  

                source_quantity = value * ureg(source_unit)
                result_quantity = source_quantity.to(target_unit)

                # Format the response
                response_text = (
                    f"{value:.2f} {source_quantity.units} = {result_quantity.magnitude:.2f} {result_quantity.units}"
                )

            # Case 2: UUID Generation
            elif query_name == "uuid.generate":
                generated_uuid = uuid.uuid4()
                response_text = f"{generated_uuid}"

            else:
                raise ValueError("Unsupported query format")

            # Add the TXT response
            response.add_answer(RR(query_name, QTYPE.TXT, rdata=TXT(response_text)))
        except Exception as e:
            # Handle errors
            response.add_answer(RR(query_name, QTYPE.TXT, rdata=TXT(f"Error: {str(e)}")))

        return response

# Start the DNS server
resolver = CustomDNSResolver()
server = DNSServer(resolver, port=5353, address="0.0.0.0", tcp=False)
print("Starting DNS server on 0.0.0.0:5353...")
server.start()