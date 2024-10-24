import json


def create_vcard_entry(name, phone):
    vcard_entry = f"""
BEGIN:VCARD
VERSION:3.0
FN:{name}
N:{name};;;
TEL;TYPE=CELL:{phone}
END:VCARD
"""
    return vcard_entry.strip()


def generate_vcards_from_json(json_file, output_file):
    with open(json_file, "r") as file:
        contacts = json.load(file)

    with open(output_file, "w") as vcf_file:
        for contact in contacts:
            name = contact.get("name", "")
            phone = contact.get("phone", "")

            if name and phone:
                vcard_entry = create_vcard_entry(name, phone)
                vcf_file.write(vcard_entry + "\n")

    print(f"All contacts saved in {output_file}")


# Replace 'contacts.json' with the path to your JSON file, and 'all_contacts.vcf' is the output file
generate_vcards_from_json("contact.json", "Final.vcf")
