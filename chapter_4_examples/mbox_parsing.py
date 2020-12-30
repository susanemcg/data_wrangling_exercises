# https://pymotw.com/2/mailbox/
# note that whatever you end up doing, it will parse the entire mailbox every time
# given that I only had 194 actual messages, but almost 8000 when you counted
# spam and promotions, makes sense to filter ahead of time if possible

import mailbox
import base64
from mimetypes import guess_extension, guess_type

example_inbox = mailbox.mbox("sample_inbox.mbox")

# iterate over all messages
# might want to do some filtering here!!
# so for gmail, it appears that your created labels are standalone (e.g. Needs Reply)
# service-applied categories are preceded by "Category" (e.g. Category Promotions)
# also: Category Personal, Category Updates, Category Purchases
# Important, Opened, Unread, Spam, Trash
for msg in example_inbox.itervalues():
    gmail_labels = msg['X-Gmail-Labels']
    # if 'Inbox' in gmail_labels:
    #     if 'Opened' in gmail_labels:
    #         print(gmail_labels)
    if 'Trash' in gmail_labels:
        print(msg['Subject'])
        # ht http://www.relevantmisc.com/scraping/2020/01/29/processing-mbox/
        # this is the basic contents, the closest to text/plain
        # might want to be more official than this
        # i guess if multipart is true, then [0] is text/plain_msg
        # this would throw an error on non-multipart
        plain_msg = msg.get_payload()[0]
        # these are the docs I need: https://docs.python.org/3/library/email.message.html
        # print(plain_msg.items())
        encoding = plain_msg.get('Content-Transfer-Encoding')
        if encoding == 'base64':
            # base64 refresher: https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
            # decoding images: https://stackoverflow.com/questions/16214190/how-to-convert-base64-string-to-image
            # imgdata = base64.b64decode(plain_msg.get_payload())
            # filename = 'some_image.gif'  # I assume you have a way of picking unique filenames
            # with open(filename, 'wb') as f:
            #     f.write(imgdata)
            # guessing mimetypes
            print(mimetypes.guess_type(plain_msg.get_payload()))
        else:
            print(plain_msg.get_payload())

        print('------------------')
