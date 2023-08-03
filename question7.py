import re
emails = ["abc@gmail.com", "123$tt*@xyz.com", "good@bad@uk.in", "nasa@usa12.space", "no-reply@domain.in", "ramhanuman@saketa.lok", "ruhi.mohan@exter123.123", "fake@fake123.fakercom"]

pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,5}$"
valid_emails = [email for email in emails if re.match(pattern, email)]

print(valid_emails)