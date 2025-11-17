import re

social_section = '''            <!-- SOCIAL -->
            <tr>
              <td align="center" style="padding:10px 0 22px 0;">
                <p style="margin:0 0 8px 0; font-size:14px; color:#6b6b6b;">
                  <strong>Join thousands of other wood carving enthusiasts on <em>WCI's</em> social media accounts!</strong>
                </p>
                <table role="presentation" border="0" cellspacing="0" cellpadding="0" style="display:inline-block;">
                  <tr>
                    <td style="padding:0 8px; text-align:center;">
                      <a href="http://facebook.com/WCIMag" target="_blank" rel="noopener" style="text-decoration:none;">
                        <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Facebook_colored_svg_copy-512.png" width="28" height="28" alt="Facebook Woodcarving Illustrated" style="display:block; border-radius:3px; margin:0 auto;">
                        <span style="display:block; font-size:10px; color:#6B6B6B; margin-top:4px;">WCI Page</span>
                      </a>
                    </td>
                    <td style="padding:0 8px; text-align:center;">
                      <a href="https://www.facebook.com/FoxChapelPublishing" target="_blank" rel="noopener" style="text-decoration:none;">
                        <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Facebook_colored_svg_copy-512.png" width="28" height="28" alt="Facebook Fox Chapel Publishing" style="display:block; border-radius:3px; margin:0 auto;">
                        <span style="display:block; font-size:10px; color:#6B6B6B; margin-top:4px;">Fox Chapel</span>
                      </a>
                    </td>
                    <td style="padding:0 8px; text-align:center;">
                      <a href="https://www.facebook.com/groups/woodcarvingillustratedmagazine" target="_blank" rel="noopener" style="text-decoration:none;">
                        <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Facebook_colored_svg_copy-512.png" width="28" height="28" alt="Facebook Woodcarving Group" style="display:block; border-radius:3px; margin:0 auto;">
                        <span style="display:block; font-size:10px; color:#6B6B6B; margin-top:4px;">WCI Group</span>
                      </a>
                    </td>
                    <td style="padding:0 8px; text-align:center;">
                      <a href="https://www.pinterest.com/woodcarvingillustratedmag" target="_blank" rel="noopener" style="text-decoration:none;">
                        <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Pinterest_colored_svg-512.png" width="28" height="28" alt="Pinterest" style="display:block; border-radius:3px; margin:0 auto;">
                        <span style="display:block; font-size:10px; color:#6B6B6B; margin-top:4px;">Pinterest</span>
                      </a>
                    </td>
                    <td style="padding:0 8px; text-align:center;">
                      <a href="https://www.instagram.com/woodcarvingillustrated" target="_blank" rel="noopener" style="text-decoration:none;">
                        <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Instagram_colored_svg_1-512.png" width="28" height="28" alt="Instagram" style="display:block; border-radius:3px; margin:0 auto;">
                        <span style="display:block; font-size:10px; color:#6B6B6B; margin-top:4px;">Instagram</span>
                      </a>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

'''

files = {
    'Renewal_WCIM_25WE3(4ED)_Compact.html': r'(<!-- ===== ADDRESS TABLE ===== -->)',
    'Renewal_WCIM_25WE4(4ED)_Compact.html': r'(<!-- ===== ADDRESS TABLE ===== -->)',
    'Renewal_WCIM_25WE5(4ED)_Compact.html': r'(<!-- ADDRESS TABLE -->)'
}

for filename, pattern in files.items():
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove existing SOCIAL section if it exists after address (between address and footer)
    content = re.sub(r'\s*<-a SOCIAL -->.*?</tr>\s*(?=\s*<!-- ========== FOOTER|<!-- FOOTER)', '', content, flags=re.DOTALL)
    
    # Insert SOCIAL section before ADDRESS TABLE
    content = re.sub(
        pattern,
        social_section + r'\1',
        content
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filename}")

print("\nAll files updated successfully!")
