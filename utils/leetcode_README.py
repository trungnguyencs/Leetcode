from pathlib import Path
import collections

class Problem:
  def __init__(self, id, originTitle, difficulty, isSolved, premium):
    self.id = id
    self.originTitle = originTitle
    self.difficulty = difficulty
    self.isSolved = isSolved
    self.premium = premium
    self.title = self.getTitle(originTitle)
    self.lastSolved = lastSolvedDic[id]
    self.markdown = self.getMarkdown(id, originTitle, self.title, difficulty, premium, self.lastSolved)
    
  def getMarkdown(self, id, originTitle, title, difficulty, premium, lastSolved):
    leetcodeUrl = "|[{id}. {originTitle}](https://leetcode.com/problems/{title}/)".format(id=id, originTitle=originTitle.replace('`', '-'), title=title)
    titleWithId = id.zfill(4) + '-' + title
    githubUrl = '' if not lastSolved else "[{titleWithId}.py](https://github.com/trungnguyencs/Leetcode/blob/main/{titleWithId}/{titleWithId}.py/)|".format(titleWithId=titleWithId)
    return '|'.join([leetcodeUrl, difficulty, premium, lastSolved, githubUrl])

  def getTitle(self, originTitle):
    title = originTitle.lower()
    for ch in '(),\'`':
      title = title.replace(ch, '')
    title = title.replace(' - ', ' ')
    title = title.replace(' ', '-')
    return title

def processTitle(line):
  id, originTitle = line.split('.')
  id, originTitle = id.strip(), originTitle.strip()
  return id, originTitle

def getQuestionIdList(path):
  txt = Path(path).read_text().split('\n')
  idList = []
  for i in range(0, len(txt), 3):
    id, originTitle = processTitle(txt[i].strip())
    idList.append(id)
  return set(idList)

def getlastSolvedDic(path):
  txt = Path(path).read_text().split('\n')
  dic = collections.defaultdict(str)
  for i in range(0, len(txt), 3):
    line = txt[i].strip()
    id = line.split('-')[0].lstrip('0')
    timestamp = txt[i+2].strip()
    dic[id] = timestamp
  return dic

premiumIds = getQuestionIdList("premium.txt")
solvedIds = getQuestionIdList("solved.txt")
lastSolvedDic = getlastSolvedDic("inGithub.txt")

path = "all.txt"
txt = Path(path).read_text().split('\n')
allProblems = []
for i in range(0, len(txt), 3):
  id, originTitle = processTitle(txt[i].strip())
  acceptanceRate = txt[i+1].strip()
  difficulty = txt[i+2].strip()
  allProblems.append(Problem(id, originTitle, difficulty, isSolved=str(id in solvedIds), premium="Premium" if id in premiumIds else ''))

allProblems.sort(key=lambda p: int(p.id))
solvedProblems = list(filter(lambda p: p.isSolved=='True', allProblems))
githubProblems = list(filter(lambda p: p.lastSolved != '', allProblems))

markdownLines = [p.markdown for p in solvedProblems]

headerPath = "readmeHeader.txt"
header = Path(headerPath).read_text()
header = header.replace("solvedProblemCount", str(len(solvedProblems))).replace("githubProblemCount", str(len(githubProblems)))
readmeStr = header + '\n' + '\n'.join(markdownLines)

readmePath = r"../README.md"
with open(readmePath, "w") as f:
    f.write(readmeStr)
