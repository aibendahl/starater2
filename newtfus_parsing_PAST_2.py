# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 23:16:02 2023

@author: Andrew
"""
from selenium import webdriver
import pandas as pd
import os
from datetime import date, timedelta
from selenium.webdriver.common.action_chains import ActionChains
import re
import time
import numpy as np
import matplotlib.pyplot as plt
import winsound
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import winsound
from difflib import SequenceMatcher
from selenium.webdriver.chrome.service import Service

os.chdir("C:/Users/Andrew/OneDrive/Desktop/Horses")
table = pd.read_excel("template3.xlsx")

service = Service(executable_path=r'C:/Users/Andrew/OneDrive/Desktop/Horses/chromedriver.exe')
browser = webdriver.Chrome(service=service)


url = "https://www.drf.com/login"
browser.get(url)

time.sleep(15)

browser.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div[1]').click()
browser.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div[1]/input').send_keys('dmaragona@gmail.com')
browser.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div[2]').click()
browser.find_element(By.XPATH,'//*[@id="password"]').send_keys('B3l1nd@26!')

time.sleep(30)

def get_past_opening_screen():
    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div[5]/div/div[1]').click()
    except Exception:
        pass
    
    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div[6]/div/div[1]').click()
    except Exception:
        pass
    
    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[3]/div[2]/div[5]/div/div[1]').click()
    except Exception:
        pass
    
    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/a').click()
    except Exception:
        pass
    
    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[3]/div[2]/a').click()
    except Exception:
        pass 
    
    time.sleep(3)
    
    browser.find_element(By.XPATH,'//html/body/div[1]/div/div[2]/div/button').click()
    
    time.sleep(15)
    
    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div[5]/div/div[1]').click()
    except Exception:
        pass
    
    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div[6]/div/div[1]').click()
    except Exception:
        pass
    
    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div[5]/div/div[1]').click()
    except Exception:
        pass
    
    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div[6]/div/div[1]').click()
    except Exception:
        pass
    
    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[3]/div[2]/div[5]/div/div[1]').click()
    except Exception:
        pass
    
    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/a').click()
    except Exception:
        pass
    
    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[3]/div[2]/a').click()
    except Exception:
        pass 
get_past_opening_screen()

time.sleep(3)

Dict_distance = {'1F': 1, '2F': 2, '21/2F': 2.5, '31/2F': 3.5,  '4F': 4, '41/2F': 4.5, '5F': 5, '51/2F': 5.5, '6F': 6,
                 '61/2F': 6.5, '63/4 F': 6.75, '7F': 7, '71/2F': 7.5, '1M': 8, '1M': 8, '11/16M': 8.5,
                 '1M_70Y': 8, '1M_40Y': 8, '11/8M': 9, '13/16 M': 9.5,'13/16M': 9.5, '11/4M': 10,
                 '15/16M': 10.5,  '13/8M': 11, '17/1M': 11.5, '11/2M': 12,
                 '19/16M': 12.5, '15/8M': 13, '11/16M': 13.5, '13/4M': 14, 
                 '113/16M': 14.5, '17/8M': 15, '115/16M': 15.5,
                 '2M': 16, '21/8M': 17,'21/4M:': 18, '21/4M': 18, '23/8M': 19, '21/2M': 20, '25/8M': 21, '23/4M': 22, '27/8M': 23,
                 '3M': 24, '21/16 M': 16.5, '2M_70Y': 2}
Dict_ML = {'1-9': 0.1,'1-5': 0.2,'2-5': 0.4,'3-5': 0.6,'1-2': 0.5,'4-5': 0.8,'1-1': 1,'6-5': 1.2,'7-5': 1.4,'8-5': 1.6,'9-5': 1.8,
           '2-1': 2,'5-2': 2.5,'3-1': 3,'7-2': 3.5,'4-1': 4,'9-2': 4.5,'5-1': 5,'6-1': 6,'7-1': 7,'8-1': 8,'9-1': 9,'10-1': 10,
           '1/5:': 0.2, '2/5:': 0.4, '3/5:': 0.6, '4/5:': 0.8, '6/5:': 1.2, '7/5:': 1.4, '8/5:': 1.6, '9/5:': 1.8,
           '3/2:': 1.5, '5/2:': 2.5, '7/2:': 3.5, '9/2:': 4.5,
           '11-1': 11,'12-1': 12,'13-1': 13,'14-1': 14,'15-1': 15,'16-1': 16, '17-1': 17, '18-1': 18,'20-1': 20,'25-1': 25,'33-1': 33,
           '50-1': 50,'30-1': 30,'35-1': 35,'40-1': 40,'99-1': 99,'3-2': 1.5, '1/2': 0.5, '19-1': 19, '21-1': 21, '22-1': 22,
           '23-1': 23,'24-1': 24,'26-1': 26,'27-1': 27,'28-1': 28,'29-1': 29,'31-1': 31,'32-1': 32,'33-1': 33,'34-1': 34,
           '36-1': 36,'37-1': 37,'38-1': 38,'39-1': 39,'41-1': 41,'42-1': 42,'43-1': 43,'44-1': 44,'45-1': 45,'46-1': 46,
           '47-1': 47,'48-1': 48,'49-1': 49,'99-1': 99, 'SCR': "SCR",
           '10/1': 10,'12/1': 12,'15/1': 15,'2/1': 2,'3/1': 3,'4/1': 4,'5/1': 5,'6/1': 6,'7/1': 7,'8/1': 8,'9/1': 9, '54-1':54}


def get_all_payouts():
    element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-event-type="CLICK_ON_FORMULATOR_PP_TAB"]')))
    element.click()
    current_url = browser.current_url
    url_parts = current_url.split('/')
    track_code = url_parts[-4] 
    race_number = url_parts[-3]  
    global cumulative_exotic_payouts
    element = browser.find_element(By.CLASS_NAME, 'raceResultWagers')
    
    # Extract the text from the element
    payoffs_text = element.text.lower()  # Convert entire text to lowercase
    #print("Raw payoffs text:", payoffs_text)  # Print the raw text for inspection
    
    # Initialize variables for payouts, starting at 0.0
    exacta_payout = 0.0
    trifecta_payout = 0.0
    pick_three_payout = 0.0
    daily_double_payout = 0.0
    grand_slam_payout = 0.0
    pick_four_payout = 0.0
    pick_five_payout = 0.0
    pick_six_payout = 0.0

    # Function to normalize wager names
    def normalize_wager_name(wager_name):
        wager_name = wager_name.lower().strip()
        if "pick" in wager_name:
            if "three" in wager_name or "3" in wager_name:
                return "pick three"
            elif "four" in wager_name or "4" in wager_name:
                return "pick four"
            elif "five" in wager_name or "5" in wager_name:
                return "pick five"
            elif "six" in wager_name or "6" in wager_name:
                return "pick six"
        return wager_name

    # Parsing function with an improved regex pattern
    def parse_race_result_wagers(input_string):
        # Improved pattern to match wager name and payouts, ignoring extra text after "paid"
        pattern = r'\$(\d+\.?\d*)\s*([\w\s]+?)\s*\(.*?\)\s*paid[:\s]*\$([\d,\.]+)'

        # Find all matches
        matches = re.findall(pattern, input_string)
        
        #print("Matches found:", matches)  # Print the matches to debug
        
        # Convert the results to a dictionary for easier lookup
        result_dict = {}
        for match in matches:
            dollar_amount = float(match[0])  # Convert the first group to a float
            wager_name = normalize_wager_name(match[1])  # Normalize wager name
            paid_amount_str = match[2].replace(',', '').strip()  # Remove commas and any trailing spaces
            paid_amount = float(paid_amount_str.rstrip('.'))  # Convert the paid amount to a float, stripping trailing periods
            
            if wager_name not in result_dict:
                result_dict[wager_name] = []
            result_dict[wager_name].append({
                'DollarAmount': dollar_amount,
                'PaidAmount': paid_amount,
            })
        
        #print("Parsed results dictionary:", result_dict)  # Print parsed results for debugging
        
        return result_dict

    # Parse the text to get the wager results
    parsed_results_dict = parse_race_result_wagers(payoffs_text)
    
    # Function to calculate payout or return 0.0 if not present
    def get_payout(wager_name):
        wager_name = normalize_wager_name(wager_name)  # Normalize the wager name again
        if wager_name in parsed_results_dict:
            payout = parsed_results_dict[wager_name][0]  # Get the first (and likely only) match
            return (1 / payout['DollarAmount']) * payout['PaidAmount']
        return 0.0
    
    # Calculate payouts for each wager
    exacta_payout = get_payout("exacta")
    trifecta_payout = get_payout("trifecta")
    pick_three_payout = get_payout("pick three")
    daily_double_payout = get_payout("daily double")
    grand_slam_payout = get_payout("grand slam")
    pick_four_payout = get_payout("pick four")
    pick_five_payout = get_payout("pick five")
    pick_six_payout = get_payout("pick six")

    # Create a single-row DataFrame
    exotics_to_be_added = pd.DataFrame({
        'Track': track_code,
        'Race': race_number,
        'Exacta': exacta_payout,
        'Trifecta': trifecta_payout,
        'Double_Pay': daily_double_payout,
        'P3_Pay': pick_three_payout,
        'P4_Pay': pick_four_payout,
        'P5_Pay': pick_five_payout,
        'P6_Pay': pick_six_payout,
        'GS_Pay': grand_slam_payout
    }, index=[0])  # Adding an index to create a single-row DataFrame
    
    
    
    table = browser.find_element(By.CLASS_NAME, "winnerListTable")
    
    # Initialize variables
    win_horse = place_horse = show_horse = None
    winner_win_pay = winner_place_pay = winner_show_pay = None
    placer_place_pay = placer_show_pay = show_payout = None
    win_horse_name = place_horse_name = show_horse_name = None
    
    # Loop through each row in the table
    rows = table.find_elements(By.CLASS_NAME, "winnerRow")
    for row in rows[1:]:  # Skip the header row
        rank = row.find_element(By.CLASS_NAME, "rank").text
        program_number = row.find_element(By.CLASS_NAME, "programNo").text
        horse_name = row.find_element(By.CLASS_NAME, "horseName").text.strip('- ')
    
        # Extract payouts with checks for empty values
        win_payoff = row.find_element(By.CLASS_NAME, "winV").text if row.find_element(By.CLASS_NAME, "winV").text else None
        place_payoff = row.find_element(By.CLASS_NAME, "placeV").text if row.find_element(By.CLASS_NAME, "placeV").text else None
        show_payoff = row.find_element(By.CLASS_NAME, "showV").text if row.find_element(By.CLASS_NAME, "showV").text else None
    
        if "1st" in rank:
            win_horse = program_number
            win_horse_name = horse_name
            winner_win_pay = win_payoff
            winner_place_pay = place_payoff
            winner_show_pay = show_payoff
        elif "2nd" in rank:
            place_horse = program_number
            place_horse_name = horse_name
            placer_place_pay = place_payoff
            placer_show_pay = show_payoff
        elif "3rd" in rank:
            show_horse = program_number
            show_horse_name = horse_name
            show_payout = show_payoff
    
    # Create a single-row DataFrame with an explicit index
    wps_to_be_added = pd.DataFrame({
        'Track': [track_code],
        'Race': [race_number],
        'Win': [win_horse],
        'Place': [place_horse],
        'Show': [show_horse],
        'W_W_Pay': [winner_win_pay],
        'W_P_Pay': [winner_place_pay],
        'W_S_Pay': [winner_show_pay],
        'P_P_Pay': [placer_place_pay],
        'P_S_Pay': [placer_show_pay],
        'S_S_Pay': [show_payout]
    })
    
    # Concatenate the new data to the existing DataFrame
    global wps_information  # Ensure wps_information is accessible globally if needed
    wps_information = pd.concat([wps_information, wps_to_be_added], ignore_index=True)
    #print(wps_information)
    cumulative_exotic_payouts = pd.concat([cumulative_exotic_payouts, exotics_to_be_added], ignore_index=True)
    #print(cumulative_exotic_payouts)
    global merged_df
    merged_df = pd.merge(wps_information, cumulative_exotic_payouts,  on=['Track', 'Race'], how='inner')
    #print(merged_df)
    global final_merged_df


def check_win(row):
    key = (row['Track'], row['Race'])
    return int(row['SaddleNumber'] == race_winners.get(key, None))    


def get_each_horse_odds():
    current_url = browser.current_url
    url_parts = current_url.split('/')
    track_code = url_parts[-4] 
    race_number = url_parts[-3]  
    # Locate the table by its ID
    table1 = browser.find_element(By.ID, 'raceChartContent')
    
    # Find all rows in the table body
    rows = table1.find_elements(By.CSS_SELECTOR, 'ul.tableBody > li.d-flex')
    
    # Initialize lists to store the data
    horses = []
    odds = []
    
    # Loop through each row and extract the relevant data
    for row in rows:
        # Extract the Horse name
        horse = row.find_element(By.CSS_SELECTOR, '.horseName a').text
        
        # Extract the Odds $1 value
        odds_value = row.find_element(By.CSS_SELECTOR, '.text-right.odds').text
        
        # Append the extracted data to the respective lists
        horses.append(horse)
        odds.append(odds_value)
    
    # Create a DataFrame with the extracted data
    

    each_horse_odds = pd.DataFrame({
        'Track': track_code,
        'Race': race_number,
        'Horse': horses,
        'Odds$1.': odds
    })
    global cumulative_each_horse_odds
    cumulative_each_horse_odds = pd.concat([cumulative_each_horse_odds,each_horse_odds], ignore_index = True)
    element_x = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-event-type="CLICK_ON_TFUS_PP_TAB"]')))
    element_x.click()


def get_new_tfus_information():    
    global cumulative_horse_info
    global cumulative_race_info
    
    try:
        element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-event-type="CLICK_ON_TFUS_PP_TAB"]')))
        element.click()
        
        current_url = browser.current_url
        url_parts = current_url.split('/')
        track_code_from_url = url_parts[-4] 
        race_number_from_url = url_parts[-3]  
        
        try:
            browser.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/label/div[1]/span').click()
            element2 = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div[4]/button'))
            )
            element2.click()    
        except Exception:
            pass
        
        try:
            browser.find_element(By.XPATH,'//*[@id="earlyPace"]').click()
            time.sleep(2)
            div_element = browser.find_element(By.CLASS_NAME, 'paceProjectorDiagram')
            projector_text = div_element.text
            possible_text_values = ['No Speed', 'Favors Frontrunners', 'Fast Pace']
        
            pace_setup = ""
            for value in possible_text_values:
                if value in projector_text:
                    pace_setup = value
                    break
                else:
                    pace_setup = 'Normal'
            if pace_setup == 'Favors Frontrunners':
                pace_setup2 = 'Favors_Early_Lead'
            else:    
                pace_setup2 = pace_setup.replace(' ', '_')
        except Exception:
            pass
            pace_setup2 = 'Unknown'
        
        time.sleep(2)
        browser.find_element(By.XPATH,'//*[@id="finishPace"]').click()
        time.sleep(2)
        
        
        # Locate the rowWrapper element
        row_wrapper = browser.find_element(By.CLASS_NAME,'rowWrapper')
        
        # Find all saddleWrap elements within the rowWrapper
        saddle_wraps = row_wrapper.find_elements(By.CLASS_NAME,'saddleWrap')
        
        # Dictionary to store the results
        results_dict = {}
        
        # Iterate through each saddleWrap and extract the required information
        for saddle_wrap in saddle_wraps:
            # Extract the 'right' style property (assuming it's always present)
            style = saddle_wrap.get_attribute('style')
            right_px = float(style.split('right:')[1].split('px')[0].strip())
            
            # Find the saddleNumber element within the current saddleWrap
            saddle_number = saddle_wrap.find_element(By.CLASS_NAME,'saddleNumber')
            number_text = saddle_number.text.strip()
            
            # Store the information in the dictionary
            results_dict[number_text] = right_px
        
        # Print the results dictionary
        #print(results_dict)
        
        div_element_count = browser.find_element(By.CSS_SELECTOR, 'div.tfusShowHorseList')
        
        li_elements = div_element_count.find_elements(By.TAG_NAME, 'li')
        number_of_entries = len(li_elements)
        
        
        div_element_scratches = browser.find_element(By.CSS_SELECTOR, 'div.saddleList')
        child_divs = div_element_scratches.find_elements(By.CSS_SELECTOR, 'div.saddleNumber')
        scratches = len(child_divs)
        
        runners = number_of_entries - scratches
        
        
        # Step 1: Sort the dictionary by its values
        sorted_results = sorted(results_dict.items(), key=lambda item: item[1])
        
        # Step 2: Extract the keys (number_text) corresponding to the lowest values
        if runners == 2:
            try:
                tf_first = sorted_results[0][0]
                tf_second = sorted_results[1][0]
                tf_third = None
                tf_fourth = None
                tf_fifth = None
                gap_1st2nd = sorted_results[1][1] - sorted_results[0][1]
                gap_2nd3rd = 0
                gap_1st3rd = 0
                gap_3rd4th = 0
                gap_1st5th = 0
            except: 
                tf_first = None
                tf_second = None       
                tf_third = None
                tf_fourth = None
                tf_fifth = None
                gap_1st2nd = 0
                gap_2nd3rd = 0     
                gap_1st3rd = 0
                gap_3rd4th = 0
                gap_1st5th = 0 
            
        if runners == 3:
            try:
                tf_first = sorted_results[0][0]
                tf_second = sorted_results[1][0]       
                tf_third = sorted_results[2][0]
                tf_fourth = None
                tf_fifth = None
                gap_1st2nd = sorted_results[1][1] - sorted_results[0][1]
                gap_2nd3rd = sorted_results[2][1] - sorted_results[1][1]      
                gap_1st3rd = sorted_results[2][1] - sorted_results[0][1]
                gap_3rd4th = 0
                gap_1st5th = 0
            except:
                tf_first = None
                tf_second = None       
                tf_third = None
                tf_fourth = None
                tf_fifth = None
                gap_1st2nd = 0
                gap_2nd3rd = 0     
                gap_1st3rd = 0
                gap_3rd4th = 0
                gap_1st5th = 0 
            
            
        if runners == 4:
            try: 
                tf_first = sorted_results[0][0]
                tf_second = sorted_results[1][0]       
                tf_third = sorted_results[2][0]
                tf_fourth = sorted_results[3][0]
                tf_fifth = None
                gap_1st2nd = sorted_results[1][1] - sorted_results[0][1]
                gap_2nd3rd = sorted_results[2][1] - sorted_results[1][1]    
                gap_3rd4th = sorted_results[3][1] - sorted_results[2][1]
                gap_1st4th = sorted_results[3][1] - sorted_results[0][1]
                gap_1st3rd = sorted_results[2][1] - sorted_results[0][1]
                gap_1st5th = 0
            except: 
                tf_first = None
                tf_second = None       
                tf_third = None
                tf_fourth = None
                tf_fifth = None
                gap_1st2nd = 0
                gap_2nd3rd = 0     
                gap_1st3rd = 0
                gap_3rd4th = 0
                gap_1st5th = 0 
         
        if runners >= 5:
            try:
                tf_first = sorted_results[0][0]
                tf_second = sorted_results[1][0]       
                tf_third = sorted_results[2][0]
                tf_fourth = sorted_results[3][0]
                tf_fifth = sorted_results[4][0]
                gap_1st2nd = sorted_results[1][1] - sorted_results[0][1]
                gap_2nd3rd = sorted_results[2][1] - sorted_results[1][1] 
                gap_3rd4th = sorted_results[3][1] - sorted_results[2][1]
                gap_1st4th = sorted_results[3][1] - sorted_results[0][1]
                gap_1st5th = sorted_results[4][1] - sorted_results[0][1]
            except:
                tf_first = None
                tf_second = None       
                tf_third = None
                tf_fourth = None
                tf_fifth = None
                gap_1st2nd = 0
                gap_2nd3rd = 0     
                gap_1st3rd = 0
                gap_3rd4th = 0
                gap_1st5th = 0 
        
        ul_element = browser.find_element(By.CLASS_NAME,'tfusDesktopLeftCntList')
        li_elements = browser.find_elements(By.CSS_SELECTOR, "ul.tfusDesktopLeftCntList li.singlehorseEntry")
        
        tf_first_backup = tf_first
        tf_second_backup = tf_second
        tf_third_backup = tf_third
        # Iterate through each <li> element
        for li in li_elements:
                tf_first = None
                tf_second = None
                tf_third = None
                
        for li in li_elements:
        # Try to locate the powerPickLabel within the current <li>
            try:
                power_pick_label = li.find_element(By.CSS_SELECTOR, "div.powerPickLabel span").text
                
                # Get the corresponding saddleNumber
                saddle_number = li.find_element(By.CSS_SELECTOR, "div.saddleNumber div.saddle").text
        
                # Assign the saddle number based on the powerPickLabel
                if power_pick_label == "1st":
                    tf_first = saddle_number
                elif power_pick_label == "2nd":
                    tf_second = saddle_number
                elif power_pick_label == "3rd":
                    tf_third = saddle_number
            
            except:    
                continue
            
        try:
            if tf_first is None:  # Check if tf_first is explicitly set to None
                tf_first = tf_first_backup
        except NameError:
            tf_first = tf_first_backup  # Set tf_first if it’s undefined
            
        try:
            if tf_second is None:  # Check if tf_first is explicitly set to None
                tf_second = tf_second_backup
        except NameError:
            tf_second = tf_second_backup  # Set tf_first if it’s undefined
            
        try:
            if tf_third is None:  # Check if tf_first is explicitly set to None
                tf_third = tf_third_backup
        except NameError:
            tf_third = tf_third_backup  # Set tf_first if it’s undefined
            
        """THIS IS THE RACE INFO"""
        
        # Function to process text from a given CSS selector
        def process_text(css_selector):
            element = browser.find_element(By.CSS_SELECTOR,css_selector)
            texts = element.text.split('\n')
            texts = [text.replace(' ', '_').replace('$', '').replace('K', '') for text in texts]
            if len(texts) == 2:
                return f"{texts[0]}_{texts[1]}"
            return texts[0] if texts else ''
        
        # Extract and process text from the specified elements
        first_col_text = process_text('div.trackDetailsCol.firstCol')
        second_col_text = process_text('div.trackDetailsCol.secondCol')
        third_col_text = process_text('div.trackDetailsCol.thirdCol')
        
        # Extract the numeric value from the fourth column
        fourth_col_element = browser.find_element(By.CSS_SELECTOR,'div.trackDetailsCol.fourthCol')
        numeric_value = ''.join(filter(str.isdigit, fourth_col_element.text))
        
        # Parse first_col_text to extract race_age, race_purse, and race_statebred
        parts = first_col_text.split('_')
        
        race_age = parts[0] if len(parts) > 0 else ''
        race_purse = parts[-1] if len(parts) > 1 else ''
        race_statebred = parts[1] if len(parts) == 3 else ''
        
        # Parse second_col_text to extract race_surface and race_condition
        surface_condition_parts = second_col_text.split('_')
        race_surface = surface_condition_parts[0] if len(surface_condition_parts) > 0 else ''
        race_condition = surface_condition_parts[1] if len(surface_condition_parts) > 1 else ''
        
        if any(grade in first_col_text for grade in ['G1', 'G2', 'G3']):
            race_condition = 'GradedStakes'
        
        first_underscore_index = third_col_text.find('_')
        last_underscore_index = third_col_text.rfind('_')
        
        if last_underscore_index == -1:
            # No underscore found
            track_condition = None
            distance_to_parse = third_col_text
            
        elif first_underscore_index == last_underscore_index:
            # Only one underscore found
            track_condition = third_col_text[last_underscore_index + 1:]
            distance_to_parse = third_col_text[:last_underscore_index]
        else:
            # Two underscores found
            track_condition = third_col_text[first_underscore_index + 1:]
            distance_to_parse = third_col_text[:first_underscore_index]
        
        distance_to_parse2 = Dict_distance.get(distance_to_parse,"Unknown")
        """
        this part is for the horse details
        """
        # Find all elements with the class 'tfusSingleHorseDetail'
        horse_details = browser.find_elements(By.CSS_SELECTOR,"[class^='tfusDesktopPPSectionWrap']")
        # Prepare lists to store data
        horse_names = []
        saddle_numbers = []
        morning_lines = []
        trainer_names = []
        jockey_names = []
        early_paces = []
        style_types = []
        late_paces = []
        # Iterate through each element and extract the desired information
        for horse in horse_details:
            try:
                # Find the title within the current horse detail element
                title = horse.find_element(By.CLASS_NAME,'horseTitle').text
                # Find the saddle number within the current horse detail element
                saddle_number = horse.find_element(By.CLASS_NAME,'saddleNumber').text
                try:
                    morning_line = horse.find_element(By.CLASS_NAME,'horseCommonWrap').text
                    morning_line2 = Dict_ML.get(morning_line,"Unknown")
                except:
                    morning_line2 = 99
                try:
                    trainer_name = horse.find_element(By.CSS_SELECTOR,'div.trainerName span').text
                except:
                    trainer_name = "N/A"
                try:
                    jockey_name = horse.find_element(By.CSS_SELECTOR,'div.jockyName span').text
                except:
                    jockey_name = "N/A"
                try:
                    early_li = horse.find_element(By.XPATH,".//li[label[text()='Early:']]")
                    early_text = early_li.find_element(By.TAG_NAME,'span').text
                except:
                    early_text = None  # Handle cases where the <li> or <span> might not be present
                try:
                    style_li = horse.find_element(By.XPATH,".//li[label[text()='Style:']]")
                    style_text = style_li.find_element(By.TAG_NAME,'span').text
                except:
                    style_text = None  # Handle cases where the <li> or <span> might not be present
                try:
                    late_li = horse.find_element(By.XPATH,".//li[label[text()='Late:']]")
                    late_text = late_li.find_element(By.TAG_NAME,'span').text
                except:
                    late_text = None  # Handle cases where the <li> or <span> might not be present
                # Append the extracted information to the lists
                horse_names.append(title)
                saddle_numbers.append(saddle_number)
                morning_lines.append(morning_line2)
                trainer_names.append(trainer_name)
                jockey_names.append(jockey_name)
                early_paces.append(early_text)
                style_types.append(style_text)
                late_paces.append(late_text)
            except:
                pass
        
        trainer_names2 = [item.replace(", II", " II") for item in trainer_names]
        # Create a DataFrame using the extracted data
        data = {
            'Horse': horse_names,
            'SaddleNumber': saddle_numbers,
            'ML': morning_lines,
            'Trainer': trainer_names2,
            'Jockey': jockey_names,
            'Early': early_paces,
            'Style': style_types,
            'Late': late_paces
        }

        horse_info = pd.DataFrame(data)
        condition = (horse_info['SaddleNumber'] == tf_first) & (horse_info['Horse'].str.contains("SCRATCHED\n", na=False))
        replacement_made = int(condition.any())
        
        horse_info.loc[horse_info['SaddleNumber'] == tf_first, 'Horse'] = horse_info.loc[horse_info['SaddleNumber'] == tf_first, 'Horse'].str.replace("SCRATCHED\n", "", regex=False)
        horse_info = horse_info[~horse_info['Horse'].str.contains("SCRATCHED\n", na=False)]
        
        horse_info['Early'] = pd.to_numeric(horse_info['Early'], errors='coerce')
        early_average = horse_info['Early'].mean()
        
        horse_info['Late'] = pd.to_numeric(horse_info['Late'], errors='coerce')
        late_average = horse_info['Late'].mean()
        
        top_early_horse = horse_info.loc[horse_info['Early'].idxmax(), 'SaddleNumber']
        top_late_horse = horse_info.loc[horse_info['Late'].idxmax(), 'SaddleNumber']
        
        top_early = horse_info['Early'].max()
        top_late = horse_info['Late'].max()
        
        horse_info['Pace_Sum'] = horse_info['Early'] + horse_info['Late']
        
        top_early_gap_avg = top_early - early_average
        top_late_gap_avg = top_late - late_average
        
        url_to_parse = browser.current_url
        parts = url_to_parse.split('/')
        race_number = parts[-3]  # Second from the right
        race_track = parts[-4]   # Third from the right
        race_number2 = "Race " + race_number
        
        distance_group = "Route" if int(distance_to_parse2) >= 8 else "Sprint"
        
        tf1_mornline = horse_info.loc[horse_info['SaddleNumber'] == tf_first, 'ML'].values[0]
        horse_info['Track'] = track_code_from_url
        horse_info['Date'] = race_date_to_pull2
        horse_info['Race'] = race_number_from_url
        horse_info['Condition'] = race_condition
        horse_info['Distance'] = distance_to_parse2
        horse_info['Surface'] = race_surface
        horse_info['Pace'] = pace_setup2
        horse_info['DistanceGroup'] = distance_group
        
        
        
        horse_column_order = ['Date','Track','Race','Condition','Distance','DistanceGroup','Surface','Pace','Horse','SaddleNumber','ML',
                              'Trainer','Jockey','Early','Style','Late','Pace_Sum']
        
        horse_info = horse_info[horse_column_order]
        gap_1st3rd = gap_1st2nd + gap_2nd3rd
        
        to_be_added = pd.DataFrame({'Date': race_date_to_pull2, 'Track': track_code_from_url, 'Race': race_number_from_url, 'ClassRating': numeric_value, 'Age': race_age,
                                   'Condition': race_condition, 'Purse': race_purse, 'Distance': distance_to_parse2,'DistanceGroup': distance_group, 'Surface': race_surface,
                                   'SurfaceCondition': track_condition,'Pace': pace_setup2, 'TF_First': tf_first,  'StateBred': race_statebred,  'Runners': runners,
                                   'TF_Second': tf_second, 'TF_Third': tf_third, 'TF_Fourth': tf_fourth, 'TF_Fifth': tf_fifth, 'Fave_ML': tf1_mornline,
                                   'FavoriteScratch': replacement_made,
                                   'Gap1_2': gap_1st2nd, 'Gap2_3': gap_2nd3rd, 'Gap1_3': gap_1st3rd, 'Gap3_4': gap_3rd4th, 'Gap1_4':gap_1st4th, 'Gap1_5':gap_1st5th}, index = [0])
        
            # Print the results
        print(f"Date: {race_date_to_pull}  Track: {race_track}  Race: {race_number2}")
        
        cumulative_horse_info = pd.concat([cumulative_horse_info,horse_info])
        cumulative_race_info = pd.concat([cumulative_race_info,to_be_added])
    except:
        pass
    #print(cumulative_race_info)

def get_filtered_race_elements():
    element_x = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-event-type="CLICK_ON_RACE_NAVIGATION"]')))
    race_elements = browser.find_elements(By.CSS_SELECTOR, "[data-event-type='CLICK_ON_RACE_NAVIGATION']")
    filtered_race_elements = []
    for li in race_elements:
        try:
            mtp_label = li.find_element(By.CSS_SELECTOR, "span.mtpLabel")
            if mtp_label.text.strip().upper() == "RESULTS":  
                filtered_race_elements.append(li)
        except:
            pass
    
    return filtered_race_elements

# Function to get the filtered li elements
def get_filtered_li_elements():
    # Find all li elements on the page
    li_elements = browser.find_elements(By.TAG_NAME, 'li')
    # Filter the li_elements based on the conditions
    filtered_li_elements = [
        li for li in li_elements
        if li.get_attribute('data-track-id') in filtered_track_ids
        and li.get_attribute('data-race-date')[-2:] == race_date_suffix
    ]
    return filtered_li_elements


def repull_historical():
    duration = 2000  # milliseconds
    freq = 440  # Hz
    #winsound.Beep(freq, duration)
    
    calendar_icon = browser.find_element(By.CLASS_NAME, "calenderIcon")
    calendar_icon.click()
    time.sleep(2)
    prev2_button = browser.find_element(By.CSS_SELECTOR, ".react-calendar__navigation__arrow.react-calendar__navigation__prev-button")
    
    for _ in range(1):
        prev2_button.click()
        time.sleep(1)
    
    day_to_click = int(race_date_to_pull[-2:])
    time.sleep(2)
    
    day_button_xpath = (
    f"//div[@class='react-calendar__month-view__days']//button["
    f".//abbr[text()='{day_to_click}'] and not(contains(@class, 'neighboringMonth')) and not(@disabled)]"
    )
    time.sleep(10)
    day_button = browser.find_element(By.XPATH, day_button_xpath)
    day_button.click()

    time.sleep(2)
    
    # Find all <li> elements with the class "pixelTracker dateItem"
    li_elements = browser.find_elements(By.CSS_SELECTOR, 'li.pixelTracker.dateItem')
    
    # Extract data-track-id values where data-race-date is "2024-06-18"
    track_ids = [
        li.get_attribute('data-track-id') 
        for li in li_elements 
        if li.get_attribute('data-race-date') == race_date_to_pull
    ]
    COUNTRYCODES = pd.read_excel("countrycodes.xlsx")
    country_codes_set = set(COUNTRYCODES['CODE'])
    global filtered_track_ids
    global race_date_suffix
    filtered_track_ids = [track_id for track_id in track_ids if track_id in country_codes_set]
    
    print(filtered_track_ids)
    
    race_date_suffix = race_date_to_pull[-2:]
    
    # Filter the li_elements based on the conditions
    filtered_li_elements = [
        li for li in li_elements
        if li.get_attribute('data-track-id') in filtered_track_ids
        and li.get_attribute('data-race-date')[-2:] == race_date_suffix
    ]

# Define a function to assign TF_Position based on conditions
def get_tf_position(row):
    if row['Win'] == row['TF_First']:
        return 1
    elif row['Win'] == row['TF_Second']:
        return 2
    elif row['Win'] == row['TF_Third']:
        return 3
    elif row['Win'] == row['TF_Fourth']:
        return 4
    elif row['Win'] == row['TF_Fifth']:
        return 5
    else:
        return 0


def get_tf_distance(row):
    if row['TF_Position'] == 1:
        return 1
    elif row['TF_Position'] == 2:
        return row['Gap1_2']
    elif row['TF_Position'] == 3:
        return row['Gap1_3']
    elif row['TF_Position'] == 4:
        return row['Gap1_4']
    elif row['TF_Position'] == 5:
        return row['Gap1_5']
    else:
        return 999


main_date_to_pull = date.today() - timedelta(days = 29)
race_date_to_pull = main_date_to_pull.strftime('%Y-%m-%d')
race_date_to_pull2 = main_date_to_pull.strftime('%m-%d-%Y')


cumulative_horse_info_STEP2 = pd.DataFrame()
cumulative_race_info_STEP2 = pd.DataFrame()
cumulative_horse_info = pd.DataFrame()
cumulative_race_info = pd.DataFrame()
cumulative_exotic_payouts = pd.DataFrame()
wps_information = pd.DataFrame()
cumulative_each_horse_odds = pd.DataFrame()
final_merged_df = pd.DataFrame()
merged_df = pd.DataFrame()
filtered_li_elements = []
    
browser.get("https://www.drf.com/classic-pp")
initial_url = "https://www.drf.com/classic-pp"

browser.maximize_window()


os.chdir("C:/Users/Andrew/OneDrive/Desktop/Horses")
repull_historical()

#len(filtered_li_elements)
#filtered_li_elements

# Get the initial filtered li elements
filtered_li_elements = get_filtered_li_elements()

#filtered_li_elements = filtered_li_elements[-4:]

# Iterate through each filtered li element
for i in range (29, 10, -1):
    main_date_to_pull = date.today() - timedelta(days = i)
    race_date_to_pull = main_date_to_pull.strftime('%Y-%m-%d')
    race_date_to_pull2 = main_date_to_pull.strftime('%m-%d-%Y')
    
    cumulative_horse_info_STEP2 = pd.DataFrame()
    cumulative_race_info_STEP2 = pd.DataFrame()
    cumulative_horse_info = pd.DataFrame()
    cumulative_race_info = pd.DataFrame()
    cumulative_exotic_payouts = pd.DataFrame()
    wps_information = pd.DataFrame()
    cumulative_each_horse_odds = pd.DataFrame()
    final_merged_df = pd.DataFrame()
    merged_df = pd.DataFrame()
    filtered_li_elements = []
    
    browser.get("https://www.drf.com/classic-pp")
    initial_url = "https://www.drf.com/classic-pp"
    
    try:
        browser.maximize_window()
    except:
        pass
    
    repull_historical()
    time.sleep(5)
    filtered_li_elements = get_filtered_li_elements()
    
    for index in range(len(filtered_li_elements)):
        if index > 0:
            repull_historical()
        
        # Re-fetch and re-filter the li elements on each iteration to avoid stale element exception
        filtered_li_elements = get_filtered_li_elements()
        #filtered_li_elements = filtered_li_elements[-4:]
        # Click on the current li element
        filtered_li_elements[index].click()
        time.sleep(8)
        try:
            element_x = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-event-type="CLICK_ON_TFUS_PP_TAB"]')))
            element_x.click()
            try:
                browser.maximize_window()
            except:
                pass
            # Wait for 12 seconds
            time.sleep(12)
            url_storage = browser.current_url
            
            try:
                element_x = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-event-type="CLICK_ON_TFUS_PP_TAB"]')))
                element_x.click()
                try:
                    svg_element = browser.find_element(By.CSS_SELECTOR, "svg.icon.iconSvg-closeThin")
                    ActionChains(browser).move_to_element(svg_element).click().perform()
                except:
                    pass
                time.sleep(3)
                pulled_race_elements = get_filtered_race_elements()
            except:
                pulled_race_elements = get_filtered_race_elements()
                
            for index in range(len(pulled_race_elements)):
                pulled_race_elements = get_filtered_race_elements()
                try:
                    element = pulled_race_elements[index]
                    element.click()
                    time.sleep(8)
            
                    # Perform actions
                    get_new_tfus_information()
                    get_all_payouts()
                    get_each_horse_odds()
                except Exception as e:
                    print(f"Error with element {index}: {e}")
        except:
            # Navigate back to the initial URL
            browser.get(url_storage)
    
        
        # Navigate back to the initial URL
        browser.get(initial_url)
        
    merged_race_level = pd.merge(cumulative_race_info, merged_df, on=['Track', 'Race'], how='inner')
    cumulative_each_horse_odds['Horse'] = cumulative_each_horse_odds['Horse'].str.replace('ë', '', regex=False)
    merged_horse_level_pre = pd.merge(cumulative_horse_info, cumulative_each_horse_odds, on=['Track', 'Race','Horse'], how='left')
    

    # Function to compute a similarity score for partial matches
    def similarity_score(source, target):
        source = ''.join(filter(str.isalpha, source)).lower()
        target = ''.join(filter(str.isalpha, target)).lower()
        return SequenceMatcher(None, source, target).ratio()
    
    
    # Copy the original DataFrame for updates
    updated_df = merged_horse_level_pre.copy()
    
    # Process each row where Odds$1. is missing
    for idx, row in updated_df[updated_df['Odds$1.'].isnull()].iterrows():
        track, race, horse = row['Track'], row['Race'], row['Horse']
        
        # Find all candidates by Track and Race
        candidates = cumulative_each_horse_odds[
            (cumulative_each_horse_odds['Track'] == track) & 
            (cumulative_each_horse_odds['Race'] == race)
        ]
        
        best_match = None
        highest_score = 0
        
        for _, candidate_row in candidates.iterrows():
            candidate_horse = candidate_row['Horse']
            score = similarity_score(horse, candidate_horse)
            if score > highest_score:
                highest_score = score
                best_match = candidate_row['Odds$1.']
        
        # Update the row with the best match if found
        if best_match is not None:
            updated_df.at[idx, 'Odds$1.'] = best_match
        else:
            print(f"ERROR: Could not find a match for Horse: {horse} in Track: {track}, Race: {race}")
    
    # Verify that all horses now have a value for Odds$1.
    if updated_df['Odds$1.'].isnull().any():
        print("Some horses still have missing Odds$1. values. Review the logic or data.")
    else:
        print("All horses now have values for Odds$1.")
    
    
    merged_horse_level = updated_df
    
    columns_to_convert = ['W_W_Pay', 'W_P_Pay', 'W_S_Pay','P_P_Pay','P_S_Pay','S_S_Pay']  # Replace with your actual column names
    
    merged_race_level[columns_to_convert] = merged_race_level[columns_to_convert].astype(float)
    
    
    merged_race_level['TF_Position'] = merged_race_level.apply(get_tf_position, axis=1)
    
    merged_race_level['TF_Distance'] = merged_race_level.apply(get_tf_distance, axis=1)
    
    race_winners = merged_race_level.set_index(['Track', 'Race'])['Win'].to_dict()
    merged_horse_level['win_check'] = merged_horse_level.apply(check_win, axis=1)
    merged_horse_level['Odds$1.'] = merged_horse_level['Odds$1.'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
    
    merged_horse_level['Return'] = merged_horse_level.apply(lambda row: row['Odds$1.'] * 2 if row['win_check'] == 1 else 0, axis=1)
    merged_horse_level['Return'] = merged_horse_level['Return'].apply(lambda x: x + 2 if x > 0 else x)
    
    merged_horse_level['top_late'] = merged_horse_level.groupby(['Date', 'Track', 'Race'])['Late'].transform(lambda x: (x == x.max()).astype(int))
    merged_horse_level['top_early'] = merged_horse_level.groupby(['Date', 'Track', 'Race'])['Early'].transform(lambda x: (x == x.max()).astype(int))
    merged_horse_level['top_total'] = merged_horse_level.groupby(['Date', 'Track', 'Race'])['Pace_Sum'].transform(lambda x: (x == x.max()).astype(int))
    
    
    deduped_race_level = merged_race_level.drop_duplicates()
    deduped_horse_level = merged_horse_level.drop_duplicates()
    
    
    os.chdir("C:/Users/Andrew/OneDrive/Desktop/Horses/RaceInfo")
    filename = "%s_races.xlsx" % race_date_to_pull
    deduped_race_level.to_excel(filename)
    
    
    os.chdir("C:/Users/Andrew/OneDrive/Desktop/Horses/HorseInfo")
    filename2 = "%s_horses.xlsx" % race_date_to_pull
    deduped_horse_level.to_excel(filename2)
    
    os.chdir("C:/Users/Andrew/OneDrive/Desktop/Horses")
    old_results = pd.read_excel("cumulative_horse_info_2025.xlsx")
    export = pd.concat([old_results, deduped_horse_level], ignore_index=True)
    export.groupby(['Date']).size()
    #export = export.drop(columns=['Unnamed: 0'])
    export.to_excel("cumulative_horse_info_2025.xlsx", index = False)
    
    
    old_results2 = pd.read_excel("cumulative_race_info_2025.xlsx")
    export2 = pd.concat([old_results2, deduped_race_level], ignore_index=True)
    export2.groupby(['Date']).size()
    #export2 = export2.drop(columns=['Unnamed: 0'])
    export2.to_excel("cumulative_race_info_2025.xlsx", index = False)
    
    time.sleep(60)


"""need to make tf_1_w, and fix the order for merged_race_level with all the payouts"""



