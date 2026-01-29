# todo_app

### repository 만들 때 처음부터 파일이 존재하게 만드는 경우 (eg. README.md 또는 License 등)
### Sourcetree 사용 시 고려할 사항
#### 1. clone으로 시작하기(원격지에 있는 파일부터 시작해서 로컬 레포지토리(아직 아무것도 없고)에 이제 막 프로젝트 시작하면 OK)
#### 2. 그런데 이미 Local repository에 이미 파일이 존재하면 Sourcetree로 pull부터 시작해도 branch가 나뉘어 있음
#### (2번과 같은 경우에는 git bash로 git cli 환경에서 명령어로 처리해야 함)

```bash
# Local repository에서
git init # .git 폴더 생성

git remote add origin <원격지 주소> # 원격지를 origin으로 부를거라고 명명. 어디로 보낼지 주소 지정해줌

git pull origin main # README.md와 License 받아옴. 원격지의 main branch

git status # staging 안 된 파일이 빨간색으로 뜸 (확인용)

git add -A # 모든 파일을 staging함(All)

git status # staging 된 파일이 초록색으로 뜸

git commit -m '<커밋 메시지>' # 커밋 메시지 작성

git status # commit 되었는지 확인

git push origin main 
```
