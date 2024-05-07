from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# ChromeOptions 객체 생성
options = Options()
# 전체화면 옵션 추가
options.add_argument("--start-maximized")

# 옵션을 포함하여 웹 드라이버 실행
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

# https://intranet.gap.com/en_us/vendor.html 웹사이트 접속
driver.get("https://intranet.gap.com/en_us/vendor.html")

# 로그인 정보
username = "Vptd325"
password = "Entks1457419!"
# 보안 질문 답변
favorite_sport_answer = "running"
first_car_make_answer = "tesla"

# 로그인 및 보안 질문 처리
while True:
    try:
        # 로그인 페이지가 로드될 때까지 대기
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "pf.username"))
        )
        break
    except TimeoutException:
        print("로그인 페이지 로드 중...")
        time.sleep(10)  # 10초 간격으로 다시 시도

# 아이디와 비밀번호 입력
driver.find_element(By.NAME, "pf.username").send_keys(username)
driver.find_element(By.NAME, "pf.pass").send_keys(password)

# 로그인 실행
driver.execute_script("postOk();")

while True:
    try:
        # 보안 질문 페이지 로드 대기
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//input[contains(@name, 'pf.challengeanswer')]"))
        )
        break
    except TimeoutException:
        print("보안 질문 페이지 로드 중...")
        time.sleep(10)  # 10초 간격으로 다시 시도

# 보안 질문 필드 확인
challenge_fields = driver.find_elements(By.XPATH, "//input[contains(@name, 'pf.challengeanswer')]")
challenge_labels = driver.find_elements(By.CLASS_NAME, "gapinc-input-label")

for i in range(len(challenge_labels)):
    if "first car" in challenge_labels[i].text.lower():
        challenge_fields[i].send_keys(first_car_make_answer)
    elif "favorite sport" in challenge_labels[i].text.lower():
        challenge_fields[i].send_keys(favorite_sport_answer)

# 보안 질문 제출
driver.execute_script("postSubmit();")

while True:
    try:
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
        break
    except TimeoutException:
        print("보안 질문 제출 후 페이지 로드 중...")
        time.sleep(10)  # 10초 간격으로 다시 시도

# Applications 드롭다운 클릭
while True:
    try:
        applications_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@title='Applications']"))
        )
        applications_menu.click()
        break
    except TimeoutException:
        print("Applications 드롭다운 로드 중...")
        time.sleep(10)  # 10초 간격으로 다시 시도

# PLM Centric 링크가 나타날 때까지 대기
while True:
    try:
        plm_centric_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@title='PLM Centric']"))
        )
        plm_centric_link.click()
        break
    except TimeoutException:
        print("PLM Centric 링크 로드 중...")
        time.sleep(10)  # 10초 간격으로 다시 시도

# PLM Centric 페이지가 로드될 때까지 대기
while True:
    try:
        WebDriverWait(driver, 10).until(EC.url_contains("/plm-centric.html"))
        print("PLM Centric 페이지로 이동했습니다.")
        break
    except TimeoutException:
        print("PLM Centric 페이지 로드 중...")
        time.sleep(10)  # 10초 간격으로 다시 시도

# PLM Centric 링크 클릭
while True:
    try:
        plm_centric_redirect_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='https://plmprod.gapinc.com/csi-requesthandler/sso/idp-redirect']"))
        )
        plm_centric_redirect_link.click()
        break
    except TimeoutException:
        print("PLM Centric 리다이렉트 링크 로드 중...")
        time.sleep(10)  # 10초 간격으로 다시 시도

# 새 창으로 전환
driver.switch_to.window(driver.window_handles[-1])

print("PLM Centric 사이트로 이동했습니다.")

# Design 링크가 나타날 때까지 대기
while True:
    try:
        design_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='MuiTab-wrapper' and @data-csi-tab-name='Design']"))
        )
        design_link.click()
        print("Design 링크를 클릭했습니다.")
        break
    except TimeoutException:
        print("Design 링크 로드 중...")
        time.sleep(10)  # 10초 간격으로 다시 시도

# OLD NAVY - WOMENS 링크가 나타날 때까지 대기
while True:
    try:
        old_navy_womens_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='browse' and @href='/WebAccess/home.html#URL=C54444590']"))
        )
        old_navy_womens_link.click()
        print("OLD NAVY - WOMENS 링크를 클릭했습니다.")
        break
    except TimeoutException:
        print("OLD NAVY - WOMENS 링크 로드 중...")
        time.sleep(10)  # 10초 간격으로 다시 시도

# BOMs 링크가 나타날 때까지 대기
while True:
    try:
        boms_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='MuiTab-wrapper' and @data-csi-tab-name='BOMs']"))
        )
        boms_link.click()
        print("BOMs 링크를 클릭했습니다.")
        break
    except TimeoutException:
        print("BOMs 링크 로드 중...")
        time.sleep(10)  # 10초 간격으로 다시 시도

# Export 드롭다운 메뉴가 나타날 때까지 대기
while True:
    try:
        export_dropdown_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='uniqName_4_61']/span[1]"))
        )
        export_dropdown_menu.click()
        print("Export 드롭다운 메뉴를 클릭했습니다.")
        break
    except TimeoutException:
        print("Export 드롭다운 메뉴 로드 중...")
        time.sleep(10)  # 10초 간격으로 다시 시도

# 클릭할 요소가 나타날 때까지 대기
while True:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[@class='dijitReset dijitMenuItemLabel' and @id='uniqName_4_58_text']"))
        )
        element.click()
        break
    except TimeoutException:
        print("클릭할 요소 로드 중...")
        time.sleep(10)  # 10초 간격으로 다시 시도

# 사용자의 입력을 기다리기 위해 대기
input("Press Enter to close the browser…")

# 웹 브라우저 종료
driver.quit()