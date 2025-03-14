# # jabber = open('Jabberwocky.txt', encoding="utf-8")
# #
# # for line in jabber:
# #     print(line.rstrip())
# #     # print(len(line))
# #
# # jabber.close()
#
# with open('Jabberwocky.txt', 'r', encoding="utf-8") as jabber:
#     # for line in jabber:
#     #     print(line.rstrip())
#     lines = jabber.readlines()
#
# print(lines)
# print(lines[-1:])
# for line in reversed(lines):
#     print(line, end='')

# with open('Jabberwocky.txt', encoding="utf-8") as jabber:
#     text = jabber.read()
#
# # print(text)
# for character in reversed(text):
#     print(character, end='')

# with open('Jabberwocky.txt', encoding="utf-8") as jabber:
#     while True:
#         line = jabber.readline().rstrip()
#         print(line)
#         if 'jubjub' in line.casefold():
#             break
#
# print('*' * 80)

with open('Jabberwocky.txt', encoding="windows-1252") as jabber:
    for line in jabber:
        print(line.rstrip())
