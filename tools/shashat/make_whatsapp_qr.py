"""Writes the WhatsApp QR shown on the About card (run on the build machine: pip install segno)."""
import sys
import segno

out = sys.argv[1] if len(sys.argv) > 1 else "Apps2Samsung.Mobile/Resources/Images/shashat_whatsapp_qr.png"
segno.make("https://wa.me/962797267922", error="m").save(out, scale=10, border=2, dark="#000000", light="#ffffff")
print("wrote", out)
