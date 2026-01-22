
import phonenumbers
from phonenumbers import geocoder, carrier

number = input("Enter phone number with country code: ")

phone = phonenumbers.parse(number)

print("Country:", geocoder.description_for_number(phone, "en"))
print("Carrier:", carrier.name_for_number(phone, "en"))
