import sys
from datetime import datetime

def add_item_to_xml(appcast, version_string, signature):

    # split version
    version, build_number = version_string.split('+')

    # get current datetime string
    current_datetime = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")

    xml_snippet = (
    "<item>\n" +
    "    <title>Version " + version +"</title>\n" +
    "    <sparkle:version>"+ build_number +"</sparkle:version>\n" +
    "    <sparkle:shortVersionString>"+ version +"</sparkle:shortVersionString>\n" +
    "    <sparkle:releaseNotesLink>\n" +
    "        https://advonext.github.io/DesktopRelease/release_notes.html\n" +
    "    </sparkle:releaseNotesLink>\n" +
    "    <pubDate>" + current_datetime + "</pubDate>\n" +
    '    <enclosure url="releases/' + version_string + '/lexnext-' + version_string + '-macos.dmg"\n' +
    '               ' + signature + '\n' +
    '               type="application/octet-stream" />\n' +
    "</item>\n"
)


    with open(appcast, 'r') as file:
        lines = file.readlines()


    lines.insert(6, xml_snippet + '\n')

    with open(appcast, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py appcast version signature")
        sys.exit(1)

    appcast = sys.argv[1]
    version = sys.argv[2]
    signature = sys.argv[3]
    add_item_to_xml(appcast, version, signature)
