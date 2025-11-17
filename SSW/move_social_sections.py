import re

social_section = '''            <!-- SOCIAL -->
            <tr>
              <td align="center" style="padding:10px 0 22px 0;">
                <p style="margin:0 0 8px 0; font-size:16px; color:#6b6b6b;; line-height:22px">
                  <strong>Join thousands of other scroll sawyers on <em>SSW's</em> social media accounts!</strong>
                </p>
                <table role="presentation" border="0" cellspacing="0" cellpadding="0" style="display:inline-block;">
                  <tr>
                    <td style="padding:0 8px; text-align:center;">
                      <a href="https://www.facebook.com/ScrollSawWoodworking" target="_blank" rel="noopener" style="text-decoration:none;">
                        <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Facebook_colored_svg_copy-512.png" width="28" height="28" alt="Facebook Scroll Saw Woodworking & Crafts" style="display:block; border-radius:3px; margin:0 auto;">
                        <span style="display:block; font-size:10px; color:#6B6B6B; margin-top:4px;">SSW Page</span>
                      </a>
                    </td>
                    <td style="padding:0 8px; text-align:center;">
                      <a href="https://www.facebook.com/FoxChapelPublishing" target="_blank" rel="noopener" style="text-decoration:none;">
                        <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Facebook_colored_svg_copy-512.png" width="28" height="28" alt="Facebook Fox Chapel Publishing" style="display:block; border-radius:3px; margin:0 auto;">
                        <span style="display:block; font-size:10px; color:#6B6B6B; margin-top:4px;">Fox Chapel</span>
                      </a>
                    </td>
                    <td style="padding:0 8px; text-align:center;">
                      <a href="https://www.facebook.com/groups/scrollsawwoodworkingcrafts" target="_blank" rel="noopener" style="text-decoration:none;">
                        <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Facebook_colored_svg_copy-512.png" width="28" height="28" alt="Facebook Scroll Saw Group" style="display:block; border-radius:3px; margin:0 auto;">
                        <span style="display:block; font-size:10px; color:#6B6B6B; margin-top:4px;">SSW Group</span>
                      </a>
                    </td>
                    <td style="padding:0 8px; text-align:center;">
                      <a href="https://www.pinterest.com/scrollsawmag" target="_blank" rel="noopener" style="text-decoration:none;">
                        <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Pinterest_colored_svg-512.png" width="28" height="28" alt="Pinterest" style="display:block; border-radius:3px; margin:0 auto;">
                        <span style="display:block; font-size:10px; color:#6B6B6B; margin-top:4px;">Pinterest</span>
                      </a>
                    </td>
                    <td style="padding:0 8px; text-align:center;">
                      <a href="https://www.instagram.com/scrollsawwoodworking" target="_blank" rel="noopener" style="text-decoration:none;">
                        <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Instagram_colored_svg_1-512.png" width="28" height="28" alt="Instagram" style="display:block; border-radius:3px; margin:0 auto;">
                        <span style="display:block; font-size:10px; color:#6B6B6B; margin-top:4px;">Instagram</span>
                      </a>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

'''

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
    
    # Remove existing SOCIAL section (after address table, before footer)
    content = re.sub(r'\s*<!-- SOCIAL -->.*?</tr>\s*(?=\s*<!-- ADDRESS|<!-- FOOTER)', '', content, flags=re.DOTALL)
    
    # Insert SOCIAL section before ADDRESS section
    # Look for ADDRESS TABLE or Customer Details comment
    content = re.sub(
        r'(<!-- ADDRESS TABLE -->|<!-- Customer Details -->)',
        social_section + r'\1',
        content
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filename}")

print("\nAll SSW files updated successfully!")
