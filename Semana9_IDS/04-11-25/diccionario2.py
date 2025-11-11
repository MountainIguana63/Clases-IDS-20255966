birtdays = {
    "Alice":"Apr 1",
    "Bob":"Dec 12",
    "Carol":"Mar 4"
}
birtdays["Carol"] = "Sep 12"
print(birtdays["Carol"])
birtdays["Pau"] = "Jul 31"
print(birtdays)
del birtdays["Bob"]
print(birtdays)

for person, date in birtdays.items():
    print(f"El cumpleaños de {person} es el día {date}.")