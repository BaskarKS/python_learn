escape_seq = 'Check Escape \'Sequence\' '
escape_seq = 'Check Escape \"Sequence\" '
escape_seq = 'Check Escape \nSequence\n '
escape_seq = 'Check Escape \\Sequence\\ '
print(escape_seq)

print("*" * 10)
print("format" + " " + "string")
print("*" * 10)
print("format" + " " + "string", "hello", end="")
print("*" * 10)
print("format" + " " + "string", "hello", sep="\n")
print("*" * 10)

variable = "10"
print(f"another {variable} way")  #format, only pass variable in parenthesis
