# 🧠 Resume Evaluation Agent

A simple and intelligent Python-based ML agent that:
- Parses resumes from local or Drive links
- Parses job descriptions
- Uses semantic similarity to score resumes from 1 to 10
- Gives one-line reasoning for the score
- Saves results to a CSV file

---

## 📁 Project Structure
resume-scanner-agent-assignment/
├── ml-agent/
│ ├── agent.py
│ ├── resume_parser.py
│ ├── job_matcher.py
│ └── utils.py
├── data/
│ ├── sample_resumes.csv
│ └── sample_job_description.txt
├── requirements.txt
├── README.md


## 📽 Demo Video

▶️ [Watch Demo Video](https://drive.google.com/file/d/1RMMD_l3j3DsBLYd6vN0aTkIwc_mi8rV_/view?usp=drive_link)  

---

## 🧪 Sample Input

**📄sample_resumes.csv`**
```csv
name,resume_link
abhishek.verma.cseaiml.2022@miet.ac.in,https://drive.google.com/uc?id=1MbaakVxXZMkqHt54NFTeGa7tGI_QRCiH
harshit.sharma.csit.2022@miet.ac.in,https://drive.google.com/open?id=1WtOp08beIhnOlt8hqoJ2yT8HdVshsvqi
umang.gupta.csit.2022@miet.ac.in,https://drive.google.com/open?id=1_FXT2Ie_ORGWivjf7aFWwg8bUhxN-G5x


**📄sample_output.csv**
name,resume_link,score,reasoning
abhishek.verma.cseaiml.2022@miet.ac.in,https://drive.google.com/uc?id=1MbaakVxXZMkqHt54NFTeGa7tGI_QRCiH,3.67,Weak match.
harshit.sharma.csit.2022@miet.ac.in,https://drive.google.com/open?id=1WtOp08beIhnOlt8hqoJ2yT8HdVshsvqi,0.03,Weak match.
umang.gupta.csit.2022@miet.ac.in,https://drive.google.com/open?id=1_FXT2Ie_ORGWivjf7aFWwg8bUhxN-G5x,0.03,Weak match.

## 🎯 Target Role(s)

- ✅ Machine Learning Engineer
- ✅ AI/ML Intern
