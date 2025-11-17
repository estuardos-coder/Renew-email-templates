import re
import os

files = [
    'Renewal_WCIM_25WE2(4ED)_Compact.html',
    'Renewal_WCIM_25WE3(4ED)_Compact.html',
    'Renewal_WCIM_25WE4(4ED)_Compact.html',
    'Renewal_WCIM_25WE5(4ED)_Compact.html'
]

def update_body_text_styling(content):
    # Update all <p> tags that don't have font-size or have different font-size
    # Pattern 1: <p style="..."> without font-size - add font-size:16px and line-height:22px
    content = re.sub(
        r'(<p style="[^"]*?)(")',
        lambda m: m.group(1) + ('; font-size:16px' if 'font-size' not in m.group(1) else '') + 
                  ('; line-height:22px' if 'line-height' not in m.group(1) else '') + m.group(2),
        content
    )
    
    # Pattern 2: Update existing font-size values to 16px and line-height to 22px in <p> tags
    content = re.sub(
        r'(<p[^>]*style="[^"]*?)font-size:\s*\d+px',
        r'\1font-size:16px',
        content
    )
    content = re.sub(
        r'(<p[^>]*style="[^"]*?)line-height:\s*\d+px',
        r'\1line-height:22px',
        content
    )
    
    # Pattern 3: Update benefit card descriptions (inside td with h3) - keep smaller text for cards
    # We'll target these specifically and keep them at a reasonable size
    # But first, let's update general p tags in benefit descriptions to 15px
    
    return content

for filename in files:
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update body text styling
    updated_content = update_body_text_styling(content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"Updated {filename}")

print("\nAll files updated successfully!")
