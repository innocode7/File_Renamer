# file_renamer.py

같은 텍스트가 있는 여러 개의 파일 이름을 한번에 변경하는 앱. 산듯한 GUI 지원

## **update history**

1. 사용자가 입력할 수 있도록 GUI 를 지원합니다.<br>
입력 항목 : directory(탐색버튼 가), old_text, new_text

2. 종료 버튼 추가

3. 명령프롬프트 미종료문제 해결<br>
스크립트가 실행 후 명령 프롬프트를 열어 두는 것 같습니다.<br>
이는 일반적으로 GUI 애플리케이션의 메인 루프(root.mainloop())가 차단되고 root.quit 메소드가 호출될 때 스크립트를 즉시 종료하지 않기 때문에 발생합니다.<br>
애플리케이션이 제대로 닫히도록 하려면 종료 버튼의 명령을 수정하여 메인 루프를 종료하고 스크립트를 닫을 수 있습니다.<br>

4. '종료' 버튼 위치 조정<br>
'파일 이름 바꾸기' 버튼 아래 있는 '종료' 버튼을 오른쪽에 배치하도록 레이아웃을 조정<br>

5. 버튼 배치, 호버 색상 변경<br>
버튼이 잘 분리되고 마우스를 올리면 색상이 변경되도록 레이아웃을 조정<br>

6. 변경할 건이 없으면 오류 표시<br>
이름을 바꾸기 전에 파일 이름에 old_text가 존재하는지 확인하기 위해 start_renaming 함수를 업데이트.<br>
파일 이름에 old_text가 포함되어 있지 않으면 사용자에게 오류 메시지가 표시됩니다.<br>

7. 파일이름 변경한 갯수 표시<br>
성공 메시지에서 성공적으로 이름이 변경된 파일 수를 표시하도록 스크립트를 업데이트<br>

## **실행 파일을 생성하는 단계별 가이드**<br>

- 파이썬 미설치 컴퓨터에서도 실행되는 원파일 만드는 방법<br>

1. 명령 프롬프트나 터미널을 엽니다.<br>

2. PyInstaller를 설치합니다:<br>
 ```PowerShell
 pip install pyinstaller
 ```
<br>
3. rename_files_gui.py가 있는 디렉터리로 이동합니다.<br>
 ```PowerShell
 cd path_to_your_script_directory
 ```
 <br>
4. PyInstaller를 실행합니다:<br>
 ```PowerShell
 pyinstaller --onefile --noconsole file_renamer.py
 ```
<br>
5. 실행 파일 찾기<br>
 프로세스가 완료되면 프로젝트 폴더 내의 dist 폴더에서 실행 파일을 찾을 수 있습니다.<br>
 실행 파일 이름은 'file_renamer.exe' (Windows의 경우)입니다.<br>

---

