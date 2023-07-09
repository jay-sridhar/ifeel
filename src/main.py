from constants import QUESTION_FORMAT, TABLE_ROW_FORMAT, INDEX_HTML_FORMAT, LIST_TEMPLATE
import csv

def generate_htmls():

    questions = []
    answers = []
    with open('resources/questionbank.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        question = None
        qid = None

        for row in reader:
            if row['question']:
                if answers:
                    questions.append({'question': question, 'qid': qid, 'answers': " ".join(answers)})
                    answers = []
                question = row['question']
                qid = row.get('\ufeffqno') or row.get('qno')
            answers.append(TABLE_ROW_FORMAT.format(**row))
        
    if answers:
        questions.append({'question': question, 'qid': qid, 'answers': " ".join(answers)})

    list_element = ''
    for question in questions:
        list_element += LIST_TEMPLATE.format(**question)
        file_name = "output/{}.html".format(question['qid'])
        with open(file_name, "w") as outfile:
            out_str = QUESTION_FORMAT.format(**question)
            outfile.write(out_str)
            print("\n\nFile name: {}\nContents: \n{}\n".format(file_name, out_str))
    with open("output/index.html", "w") as outfile:
        outfile.write(INDEX_HTML_FORMAT.format(list_element))


if __name__ == "__main__":
    generate_htmls()