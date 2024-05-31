# Obtain the user´s email
email = input("What is your email?: ")

# cut user´s name
user = email[ : email.index("@")]

# cut user´domain
domain = email[email.index("@")+1 : ]

# text format
ouput = "Your user name is {} and the domain´s name is {}".format(user, domain)

# Show ouput message
print(ouput)
