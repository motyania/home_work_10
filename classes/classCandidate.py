import json


class Candidates:
    """ Класс кандидатов """

    def __init__(self, path):
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        self.data = data

    def candidates_page(self):
        """" Возвращает перечень кандидатов """
        list_candidates = ""
        for item in self.data:
            list_candidates += "Имя кандидата - "
            list_candidates += item["name"] + "\n"
            list_candidates += item["position"] + "\n"
            list_candidates += item["skills"] + "\n\n"

        return f"<pre>{list_candidates}</pre>"

    def candidate_info(self, uid):
        """ Возвращает информацию о кандидате по id"""
        candidate_data = ""
        for item in self.data:
            if uid == item["id"]:
                candidate_data += "<img src=" + item['picture'] + ">" + "\n"
                candidate_data += "<pre>"
                candidate_data += "Имя кандидата - "
                candidate_data += item["name"] + "\n"
                candidate_data += item["position"] + "\n"
                candidate_data += item["skills"] + "\n"
                candidate_data += "</pre>"

        return candidate_data

    def skills_selection(self, skill):
        """ Возвращает перечень кандидатов по навыку """
        list_candidates = ""
        for item in self.data:
            skills_data = item["skills"].split(", ")
            skills_data = [x.lower() for x in skills_data]
            if skill.lower() in skills_data:
                list_candidates += "Имя кандидата - "
                list_candidates += item["name"] + "\n"
                list_candidates += item["position"] + "\n"
                list_candidates += item["skills"] + "\n\n"

        return f"<pre>{list_candidates}</pre>"

    def __repr__(self):
        return self.data
