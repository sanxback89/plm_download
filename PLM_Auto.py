from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time  # time.sleep을 사용하기 위해 time 모듈을 임포트합니다.

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
try:
    # 로그인 페이지가 로드될 때까지 대기
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "pf.username"))
    )

    # 아이디와 비밀번호 입력
    driver.find_element(By.NAME, "pf.username").send_keys(username)
    driver.find_element(By.NAME, "pf.pass").send_keys(password)

    # 로그인 실행
    driver.execute_script("postOk();")

    # 보안 질문 페이지 로드 대기
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//input[contains(@name, 'pf.challengeanswer')]"))
    )

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
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
except Exception as e:
    print(f"로그인 또는 보안 질문 처리 중 에러 발생: {str(e)}")

# Applications 드롭다운 클릭
try:
    applications_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='Applications']"))
    )
    applications_menu.click()

    # PLM Centric 링크가 나타날 때까지 대기
    plm_centric_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='PLM Centric']"))
    )
    # PLM Centric 링크 클릭
    plm_centric_link.click()

    # PLM Centric 페이지가 로드될 때까지 대기
    WebDriverWait(driver, 10).until(EC.url_contains("/plm-centric.html"))

    print("PLM Centric 페이지로 이동했습니다.")

    # PLM Centric 링크 클릭
    plm_centric_redirect_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='https://plmprod.gapinc.com/csi-requesthandler/sso/idp-redirect']"))
    )
    plm_centric_redirect_link.click()

    # 새 창으로 전환
    driver.switch_to.window(driver.window_handles[-1])

    print("PLM Centric 사이트로 이동했습니다.")

    # PLM Centric으로 이동한 후 페이지가 완전히 로드될 때까지 20초간 대기
    time.sleep(20)

    # Design 링크 클릭
    design_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='MuiTab-wrapper' and @data-csi-tab-name='Design']"))
    )
    design_link.click()

    print("Design 링크를 클릭했습니다.")

    # OLD NAVY - WOMENS 링크 클릭
    old_navy_womens_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='browse' and @href='/WebAccess/home.html#URL=C54444590']"))
    )
    old_navy_womens_link.click()
    print("OLD NAVY - WOMENS 링크를 클릭했습니다.")

    # BOMs 링크 클릭
    boms_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='MuiTab-wrapper' and @data-csi-tab-name='BOMs']"))
    )
    boms_link.click()
    print("BOMs 링크를 클릭했습니다.")

    # BOMs 페이지로 이동한 후 페이지가 완전히 로드될 때까지 10초간 대기
    time.sleep(10)

    print("BOMs 페이지가 로드되었습니다.")

    # Export 드롭다운 메뉴 클릭
    export_dropdown_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='uniqName_4_61']/span[1]"))
    )
    export_dropdown_menu.click()
    print("Export 드롭다운 메뉴를 클릭했습니다.")
    
    # 클릭할 요소가 나타날 때까지 최대 10초 동안 대기
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//td[@class='dijitReset dijitMenuItemLabel' and @id='uniqName_4_58_text']"))
    )

    # 요소 클릭
    element.click()

except TimeoutException:
    print("특정 요소를 찾을 수 없거나 작업 수행 중 에러가 발생했습니다.")

# 사용자의 입력을 기다리기 위해 대기

input("Press Enter to close the browser…")

# 웹 브라우저 종료
driver.quit()