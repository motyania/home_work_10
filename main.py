from flask import Flask
from classes.classCandidate import Candidates

candidate = Candidates("candidates.json")
app = Flask(__name__)


@app.route("/")
def index_page():
    return candidate.candidates_page()


@app.route("/candidate/<int:uid>")
def candidate_info(uid):
    return candidate.candidate_info(uid)


@app.route("/skill/<skill>")
def skills_selection(skill):
    return candidate.skills_selection(skill)


# app.add_url_rule('/', view_func=candidate.candidates_page)
# app.add_url_rule('/candidate/<int:uid>', view_func=candidate.candidate_info)
# app.add_url_rule('/skill/<skill>', view_func=candidate.skills_selection)

app.run()
