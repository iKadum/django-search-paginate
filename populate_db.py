from search_pagination_app.models import Post
import random
import string


POSTS_NO = 1500  # number of posts to insert into DB


def sentence(min_w, max_w, min_l, max_l):
    # return min_w to max_w number of words, each word has min_ to max_ number of letters
    words = []
    words_number = random.randint(min_w, max_w)
    for _ in range(words_number):
        word = "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(min_l, max_l)))
        words.append(word)
    return " ".join(words)


def title():
    post_title = sentence(3, 6, 1, 9)  # 3 to 6 words, each word 1 tom9 letters
    return post_title.title()


def description():
    sentences_list = []
    sentences_number = random.randint(1, 3)  # 1 to 3 sentence

    for _ in range(sentences_number):
        current_sentence = sentence(4, 12, 1, 12).capitalize() + "."
        # each sentence 4 to 12 words, each word 1 to 12 letters
        sentences_list.append(current_sentence)

    return " ".join(sentences_list)


def post():
    sentences_list = ["<p>"]  # open p tag at the start of the post
    sentences_number = random.randint(45, 75)  # 45 to 75 sentences
    paragraphs = random.randint(3, 9)  # number of paragraphs for each post
    sentences_per_paragraph = sentences_number // paragraphs

    for sentence_number in range(sentences_number):
        sentence_number += 1  # range starts form 0, so sentence number is always + 1
        current_sentence = sentence(4, 15, 1, 12).capitalize() + "."
        # each sentence 4 to 15 words, each word 1 to 12 letters
        sentences_list.append(current_sentence)

        if sentence_number % sentences_per_paragraph == 0:
            # new paragraph every sentences_per_paragraph number
            sentences_list.append("</p>\n<p>")

    if sentences_list[-1] == "</p>\n<p>":
        # no need for new paragraph at the end of the post
        sentences_list.pop()

    sentences_list.append("</p>")  # close p tag at the end of the post

    return " ".join(sentences_list)  # all sentences from list joined


# add POSTS_NO number of posts to the database
for x in range(POSTS_NO):
    title_ = title() + " (" + str(x + 1) + ")"
    description_ = description()
    post_ = post()
    p = Post(
        title=title_,
        description=description_,
        post=post_
    )

    p.save()
