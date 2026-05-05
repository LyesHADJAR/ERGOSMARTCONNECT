import re

with open('/Users/elyashadjar/Dev/ERGOSMARTCONNECT/Dashboard/templates/Messages du patient.html', 'r') as f:
    content = f.read()

# Update inline style of notificationsPanel
new_panel = """        <div id="notificationsPanel" style="
            display:none;
            position:absolute;
            right:0; top:45px;
            width:320px;
            max-width:calc(100vw - 20px);
            background:#fff;
            border-radius:16px;
            box-shadow:0 12px 30px rgba(0,0,0,.15);
            z-index:9999;
            overflow:hidden;
            border:1px solid rgba(0,0,0,.08);
        ">"""

content = re.sub(r'        <div id="notificationsPanel" style="[^"]*">', new_panel, content)

with open('/Users/elyashadjar/Dev/ERGOSMARTCONNECT/Dashboard/templates/Messages du patient.html', 'w') as f:
    f.write(content)

print("Done")
