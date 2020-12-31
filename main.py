from selenium import webdriver
import random
import time

web = webdriver.Firefox(executable_path="D:\Driver\geckodriver.exe")
web.get('https://forms.gle/FZqNYMaxvfsr9YoTA')
time.sleep(1)


def chooseAge():  # ใส่อายุ
    age = random.randint(10, 25)
    ageWeb = web.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    ageWeb.send_keys(age)


def chooseGender():  # เลือกเพศ
    gender = random.randint(1, 3)
    web.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[" + str(
            gender) + "]/label/div/div[1]/div/div[3]/div").click()


def chooseLikeAnime():  # ชอบดูอนิเมะไหม
    time.sleep(1)
    like = random.randint(1, 3)
    like = 1
    web.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/span/div/div[" + str(
            like) + "]/label/div/div[1]/div/div[3]/div").click()
    nextButton2()
    if like == 1:
        botChooseLike()
    elif like == 2:
        botChooseSoSo()
    elif like == 3:
        botChooseUnLike()


def botChooseLike():  # บอทเลือกชอบดูอนิเมะ
    time.sleep(1)
    like = random.randint(1, 2)
    web.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/span/div/div[" + str(
            like) + "]/label/div/div[1]/div/div[3]/div").click()
    botChooseCheckBox1()
    botChooseCheckBox2()
    botChooseCheckBox3()
    botChooseAnimeLC()
    botChooseAnimeWatchTime()
    botChooseAnimeWatchIn()
    botChooseCheckBox4()
    botChooseTheBestAnime()
    botChooseTheBestCharacter()
    nextButton3()

    if like == 2:
        summitButton()
    else:
        animeSeasonSummer2020()
        summitButton()


def animeSeasonSummer2020():
    for i in range(2, 23):
        scoreNull = random.randint(1, 2)
        if scoreNull == 2:
            score = random.randint(1, 5)
            web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[" + str(
                i) + "]/div/div/div[3]/div[1]/span/div/label[" + str(score) + "]/div[2]/div/div/div[3]/div").click()
    nextButton4()


def botChooseAnimeLC():  # คุณดูอนิเมะถูกลิขสิทธิ์หรือผิดอนิเมะถูกลิขสิทธิ์
    choose = random.randint(1, 4)
    web.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[" + str(
            choose) + "]/label/div/div[1]/div/div[3]/div").click()


def botChooseAnimeWatchTime():  # โดยเฉลี่ยแล้ว คุณดูอนิเมะนานแค่ไหน ( ในหนึ่งสัปดาห์ )
    choose = random.randint(1, 8)
    web.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[" + str(
            choose) + "]/label/div/div[1]/div/div[3]/div")
    web.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[" + str(
            choose) + "]/label/div/div[1]/div/div[3]/div").click()


def botChooseAnimeWatchIn():  # คุณชอบดูอนิเมะในไหนมากที่สุด
    choose = random.randint(1, 7)
    web.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[" + str(
            choose) + "]/label/div/div[1]/div/div[3]/div").click()


def botChooseTheBestAnime():  # อนิเมะที่ชอบเป็นพิเศษของคุณ คือ *
    animeList = ["Fullmetal Alchemist: Brotherhood", "Steins;Gate", "Hunter x Hunter", "Gintama",
                 "Legend of the Galactic Heroes", "Attack on Titan Season", "March Comes In Like A Lion",
                 "Your Name", "A Silent Voice", "Clannad ~After Story~", "Code Geass", "Love is War", "Vinland Saga",
                 "Kimetsu no Yaiba", "Re:ZERO", "The Promised Neverland", "JoJo's Bizarre Adventure",
                 "Fate", "One Punch Man", "Sword Art Online", "Death Note", "Tokyo Ghoul", "My Hero Academia"]
    theBestAnime = animeList[random.randint(0, 22)]
    print(theBestAnime)
    web.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(
        theBestAnime)


def botChooseTheBestCharacter():  # อนิเมะที่ชอบเป็นพิเศษของคุณ คือ *
    characterList = ["Lamperouge, Lelouch", "Lawliet, L", "Monkey D., Luffy", "Levi", "Yagami, Light", "Elric, Edward",
                     "Roronoa, Zoro", "Okabe, Rintarou", "Uzumaki, Naruto", "Zoldyck, Killua",
                     "Sakata, Gintoki", "Uchiha, Itachi", "Hikigaya, Hachiman", "Makise, Kurisu", "Kirigaya, Kazuto",
                     "Rem", "Guts", "Saitama", "Kaneki, Ken", "Ackerman, Mikasa", "Voldigoad, Anos",
                     "Echidna", "Emilia"]
    theBestCharacter = characterList[random.randint(0, 22)]
    print(theBestCharacter)
    web.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(
        theBestCharacter)


def botChooseCheckBox1():  # ชอบดูอนิเมะแนวไหน
    for i in range(1, 11):
        selectBox = random.randint(1, 2)
        if selectBox == 1:
            web.find_element_by_xpath(
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[" + str(
                    i) + "]/label/div/div[1]/div[2]").click()


def botChooseCheckBox2():  # คุณชอบพระเอกแบบไหน
    for i in range(1, 13):
        selectBox = random.randint(1, 2)
        if selectBox == 1:
            web.find_element_by_xpath(
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[" + str(
                    i) + "]/label/div/div[1]/div[2]").click()


def botChooseCheckBox3():  # คุณชอบผู้หญิงแบบไหนในอนิเมะ
    for i in range(1, 11):
        selectBox = random.randint(1, 2)
        if selectBox == 1:
            web.find_element_by_xpath(
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[" + str(
                    i) + "]/label/div/div[1]/div[2]").click()


def botChooseCheckBox4():  # ได้อะไรจากการดูอนิเมะ
    selectNone = random.randint(1, 2)
    if selectNone == 2:
        for i in range(1, 11):
            selectBox = random.randint(1, 2)
            if selectBox == 1:
                web.find_element_by_xpath(
                    "/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div[" + str(
                        i) + "]/label/div/div[1]/div[2]").click()
    else:
        web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div["
                                  "11]/label/div/div[1]/div[2]").click()


def botChooseSoSo():  # บอทเลือกเฉย ๆ กับการดูอนิเมะ
    time.sleep(1)
    choose = random.randint(2, 7)
    web.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/span/div/div[" + str(
            choose) + "]/label/div/div[1]/div/div[3]/div").click()
    nextButton6()
    waitAnime()


def waitAnime():
    choose = random.randint(1, 3)
    print(choose)
    web.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/span/div/div[" + str(
            choose) + "]/label/div/div[1]/div/div[3]/div").click()
    nextButton7()
    if choose == 1:
        botChooseLike()
    else:
        summitButton()


def botChooseUnLike():  # บอทเลือกไม่ชอบดูอนิเมะ
    time.sleep(1)
    unlike = random.randint(2, 7)
    web.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/span/div/div[" + str(
            unlike) + "]/label/div/div[1]/div/div[3]/div").click()
    nextButton5()
    summitButton()


def nextButton1():
    web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span").click()


def nextButton2():
    web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span").click()


def nextButton3():
    web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span").click()


def nextButton4():
    web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span").click()


def nextButton5():
    web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span").click()


def nextButton6():
    web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span").click()


def nextButton7():
    web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span").click()


def summitButton():
    web.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span").click()
    web.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/a[3]").click()  # ส่งคำตอบเพิ่มอีก
    main()


def main():
    chooseAge()
    chooseGender()
    nextButton1()
    chooseLikeAnime()


main()
