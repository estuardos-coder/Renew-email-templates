import re

files = [
    'Renewal_SSWC_25SE1(1ED).html',
    'Renewal_SSWC_25SE2(1ED).html',
    'Renewal_SSWC_25SE3(1ED).html',
    'Renewal_SSWC_25SE4(1ED).html',
    'Renewal_SSWC_25SE5(1ED).html'
]

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and extract the SOCIAL section
    social_match = re.search(r'(\s*<!-- SOCIAL -->.*?</tr>\s*\n)', content, flags=re.DOTALL)
    
    if social_match:
        social_section = social_match.group(1)
        
        # Remove SOCIAL section from its current location
        content = content.replace(social_section, '')
        
        # Insert SOCIAL section before FOOTER (after address section)
        content = re.sub(
            r'(\s*<!-- FOOTER -->)',
            social_section + r'\1',
            content
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated {filename} - social section moved to after address, before footer")
    else:
        print(f"No SOCIAL section found in {filename}")

print("\nAll SSW files restored to original social section placement!")
