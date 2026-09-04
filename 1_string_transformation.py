booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

booking = booking.strip()

parts = booking.split(" | ")

event_code = parts[0]
name = parts[1]
room = parts[2]
time = parts[3]
email = parts[4]
vip_tag = parts[5]

name = name.title()
room = room.upper()
email = email.lower()

event_valid = event_code.startswith("EVT-")

username_clean = name.lower()
username_clean = username_clean.replace("_", "")
username_valid = username_clean.isalpha()

room_valid = room.startswith("ROOM-")
room_number = room[5:]
room_valid = room_valid and room_number.isdigit()

time_valid = ":" in time

at_position = email.find("@")
email_domain = email[at_position + 1:]

vip_tag_lower = vip_tag.lower()
vip_count = vip_tag_lower.count("vip")

email_valid = "@" in email and "." in email

print("Event code:", event_code)
print("Name:", name)
print("Room:", room)
print("Time:", time)
print("Email domain:", email_domain)
print("VIP tag count:", vip_count)
print("Valid event code:", event_valid)
print("Valid username:", username_valid)
print("Valid room:", room_valid)
print("Valid time:", time_valid)
print("Valid email:", email_valid)