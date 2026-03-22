import segno

# 1. Your Live URL (Make sure this is your Netlify/Vercel link!)
link = "https://your-medichub-demo.vercel.app"

# 2. Generate a "Clean" QR
# Error='m' makes the pattern less dense and cleaner for printing
qrcode = segno.make(link, error='m')

# 3. Save as a high-resolution PNG
# Scale 20 makes it large and sharp for printing on bond paper
# Dark='#002D62' matches the Navy Blue in your logo
qrcode.save('logo.png', scale=20, dark='#002D62')

print("---------------------------------------")
print("SUCCESS! Clean QR code generated.")
print("File saved as: logo.png")
print("---------------------------------------")