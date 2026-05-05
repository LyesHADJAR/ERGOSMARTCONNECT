import re

with open('/Users/elyashadjar/Dev/ERGOSMARTCONNECT/Dashboard/templates/Messages du patient.html', 'r') as f:
    content = f.read()

# Update .attachment-preview
attachment_css = """        .attachment-preview{
            display:flex;
            align-items:center;
            gap:10px;
            margin-top:10px;
            padding:10px 14px;
            border-radius:12px;
            background:rgba(0,0,0,.06);
            font-size:.85rem;
            font-weight:600;
            cursor:pointer;
            text-decoration:none !important;
            color:var(--text-1) !important;
            transition:all .2s ease;
            border:1px solid rgba(0,0,0,.05);
        }

        .attachment-preview:hover{
            background:rgba(0,0,0,.09);
            transform:translateY(-1px);
        }

        .attachment-preview i{
            font-size:1.2rem;
            color:var(--primary);
        }

        .message-row.patient .attachment-preview{
            background:rgba(255,255,255,.15);
            color:#fff !important;
            border-color:rgba(255,255,255,.2);
        }

        .message-row.patient .attachment-preview:hover{
            background:rgba(255,255,255,.25);
        }

        .message-row.patient .attachment-preview i{
            color:#fff;
        }"""

content = re.sub(r'        \.attachment-preview\{[\s\S]*?\.message-row\.patient \.attachment-preview\{[^}]*\}', attachment_css, content)

# Update notification panel styles
notification_css = """.notification-item{
    padding:14px 16px;
    border-bottom:1px solid rgba(0,0,0,.06);
    cursor:pointer;
    transition:.2s ease;
    background:#fff;
}

.notification-item:hover{
    background:#f8fafc;
}

.notification-title{
    font-size:.9rem;
    font-weight:700;
    color:#0f172a;
    margin-bottom:4px;
    display:flex;
    align-items:center;
    gap:6px;
}

.notification-text{
    font-size:.85rem;
    color:#475569;
    line-height:1.45;
}

.notification-time{
    font-size:.75rem;
    color:#94a3b8;
    margin-top:8px;
    font-weight:500;
}
"""

content = re.sub(r'\.notification-item\{[\s\S]*?\.notification-time\{[^}]*\}', notification_css, content)

with open('/Users/elyashadjar/Dev/ERGOSMARTCONNECT/Dashboard/templates/Messages du patient.html', 'w') as f:
    f.write(content)

with open('/Users/elyashadjar/Dev/ERGOSMARTCONNECT/Dashboard/templates/message.html', 'r') as f:
    content2 = f.read()
    content2 = re.sub(r'        \.attachment-preview\{[\s\S]*?\.message-row\.patient \.attachment-preview\{[^}]*\}', attachment_css, content2)
    content2 = re.sub(r'\.notification-item\{[\s\S]*?\.notification-time\{[^}]*\}', notification_css, content2)

with open('/Users/elyashadjar/Dev/ERGOSMARTCONNECT/Dashboard/templates/message.html', 'w') as f:
    f.write(content2)

print("Done")
