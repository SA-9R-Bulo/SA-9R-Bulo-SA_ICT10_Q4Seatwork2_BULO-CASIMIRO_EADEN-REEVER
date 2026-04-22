from js import document

all_classmates = []

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! My name is {self.name} from section {self.section}, and my favorite subject is {self.favorite_subject}."


# ADD (same as before)
def add(event):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    if name == "" or section == "" or subject == "":
        return

    new_student = Classmate(name, section, subject)
    all_classmates.append(new_student)

    
    outputDiv = document.getElementById("classmateList")

    div = document.createElement("div")
    div.className = "list-item"
    div.innerText = new_student.introduce()

    outputDiv.appendChild(div)

    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("subject").value = ""


def show(event):
    outputDiv = document.getElementById("classmateList")
    outputDiv.innerHTML = ""

    # Show total count
    count = document.createElement("h5")
    count.innerText = f"Total Classmates: {len(all_classmates)}"
    outputDiv.appendChild(count)

    
    line = document.createElement("hr")
    outputDiv.appendChild(line)

    
    for student in all_classmates:
        div = document.createElement("div")
        div.className = "list-item"
        div.innerText = student.introduce()
        outputDiv.appendChild(div)