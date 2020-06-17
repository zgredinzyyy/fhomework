from selenium import webdriver
from time import sleep
from selenium.common.exceptions import WebDriverException

class fhomework:
    def __init__(self, url):
            self.url = url
            self.driver = webdriver.Chrome()
            self.sentences = []
            self.driver.get(self.url)
            sleep(5)
            for i in range(20):
                try:
                    self.driver.find_element_by_xpath('//*[@id="exercise"]/div/table/tbody/tr[%s]/td[2]/button[2]' % str(i+1)).click()
                except WebDriverException:
                    self.driver.find_element_by_xpath('//*[@id="main-content"]/p[4]/div/div/button')\
                        .click()
                    sleep(3)
                    continue
                self.driver.find_element_by_xpath('//*[@id="exercise"]/div/table/tbody/tr[%s]/td[2]/button[2]' % str(i+1))\
                    .click()
                sleep(1)
                sentence = self.driver.find_element_by_xpath('//*[@id="exercise"]/div/table/tbody/tr[%s]/td[1]/div[2]/span/span' % str(i+1)).text
                sentence = sentence.strip('[] ')
                self.sentences.append(sentence)

            self.driver.get(self.url)
            sleep(5)
            for i in range(20):
                try:
                    self.driver.find_element_by_xpath('//*[@id="exercise"]/div/table/tbody/tr[%s]/td[2]/button[2]' % str(i+1)).click()
                except WebDriverException:
                    self.driver.find_element_by_xpath('//*[@id="main-content"]/p[4]/div/div/button')\
                        .click()
                    sleep(3)
                    continue
                self.driver.find_element_by_xpath('//*[@id="exercise"]/div/table/tbody/tr[%s]/td[1]/div[1]/span[4]/div/input' % str(i+1))\
                    .send_keys(self.sentences[i])
                self.driver.find_element_by_xpath('//*[@id="exercise"]/div/table/tbody/tr[%s]/td[2]/button[1]' % str(i+1))\
                    .click()
            sleep(60)
                


fhomework('https://www.perfect-english-grammar.com/say-or-tell-exercise-1.html')