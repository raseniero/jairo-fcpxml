import xml.etree.ElementTree as ET
import os


def open_template(template_xml_file):
    if not os.path.exists(template_xml_file):
        raise ValueError("template file not found")
    return ET.parse(template_xml_file)


if __name__ == "__main__":
    template_xml = open_template("template.fcpxml")
    print(template_xml.getroot().find("library").find("event").find("project"))
