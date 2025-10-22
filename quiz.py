#!/usr/bin/env python3
"""
Economics 1 Quiz Application
By Sophie Kasse
A command-line quiz application for Economics 1 students
"""

import random
import json
from typing import List, Dict, Tuple

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    """Clear the terminal screen"""
    print("\n" * 50)

def print_header(text: str):
    """Print a formatted header"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'=' * 70}")
    print(f"{text.center(70)}")
    print(f"{'=' * 70}{Colors.END}\n")

def print_question(q_num: int, total: int, question: str):
    """Print a formatted question"""
    print(f"{Colors.CYAN}{Colors.BOLD}Question {q_num}/{total}{Colors.END}")
    print(f"{Colors.BOLD}{question}{Colors.END}\n")

def print_choices(choices: List[str]):
    """Print formatted answer choices"""
    for i, choice in enumerate(choices, 1):
        print(f"  {i}. {choice}")
    print()

def get_user_choice(num_choices: int) -> int:
    """Get and validate user input"""
    while True:
        try:
            choice = input(f"{Colors.YELLOW}Enter your answer (1-{num_choices}): {Colors.END}")
            choice = int(choice)
            if 1 <= choice <= num_choices:
                return choice
            else:
                print(f"{Colors.RED}Please enter a number between 1 and {num_choices}{Colors.END}")
        except ValueError:
            print(f"{Colors.RED}Please enter a valid number{Colors.END}")
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}Quiz interrupted. Exiting...{Colors.END}")
            exit(0)

def show_result(is_correct: bool, correct_answer: str, explanation: str = ""):
    """Show whether answer was correct"""
    if is_correct:
        print(f"{Colors.GREEN}{Colors.BOLD}✓ Correct!{Colors.END}")
    else:
        print(f"{Colors.RED}{Colors.BOLD}✗ Incorrect{Colors.END}")
        print(f"{Colors.YELLOW}The correct answer was: {correct_answer}{Colors.END}")
    
    if explanation:
        print(f"{Colors.CYAN}Explanation: {explanation}{Colors.END}")
    
    input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

def calculate_grade(score: int, total: int) -> Tuple[str, str]:
    """Calculate letter grade and pass/fail status"""
    percentage = (score / total) * 100
    
    if percentage >= 75:
        grade = "A"
        status = "PASSED"
    elif percentage >= 70:
        grade = "B"
        status = "PASSED"
    elif percentage >= 60:
        grade = "C"
        status = "PASSED"
    elif percentage >= 50:
        grade = "D"
        status = "PASSED"
    else:
        grade = "F"
        status = "FAILED"
    
    return grade, status

def show_final_results(score: int, total: int, test_name: str):
    """Display final test results"""
    percentage = (score / total) * 100
    grade, status = calculate_grade(score, total)
    
    clear_screen()
    print_header(f"{test_name} - RESULTS")
    
    print(f"{Colors.BOLD}Your Score: {score}/{total}{Colors.END}")
    print(f"{Colors.BOLD}Percentage: {percentage:.1f}%{Colors.END}")
    print(f"{Colors.BOLD}Grade: {grade}{Colors.END}")
    
    if status == "PASSED":
        print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 CONGRATULATIONS! YOU PASSED! 🎉{Colors.END}")
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}Unfortunately, you did not pass this time.{Colors.END}")
        print(f"{Colors.YELLOW}Keep studying and try again!{Colors.END}")
    
    print(f"\n{Colors.CYAN}Performance Analysis:{Colors.END}")
    if percentage >= 80:
        print("Excellent work! You have a strong grasp of the material.")
    elif percentage >= 70:
        print("Good job! You understand most concepts well.")
    elif percentage >= 60:
        print("Fair performance. Review the material to strengthen your understanding.")
    elif percentage >= 50:
        print("You passed, but there's room for improvement. Focus on weak areas.")
    else:
        print("More study is needed. Review all topics thoroughly.")
    
    input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

# TEST 1: MEASURING ECONOMIC PERFORMANCE
TEST_1_QUESTIONS = [
    {
        "question": "Which of the following is NOT one of the five macroeconomic objectives?",
        "choices": [
            "Economic growth",
            "Full employment",
            "Increased exports",
            "Price stability"
        ],
        "correct": 2,
        "explanation": "The five objectives are: economic growth, full employment, price stability, balance of payments stability, and equitable distribution of income."
    },
    {
        "question": "GDP is defined as:",
        "choices": [
            "Total value of all goods produced in a country",
            "Total value of all final goods and services produced within a country's boundaries in a period",
            "Total income earned by citizens",
            "Total exports minus imports"
        ],
        "correct": 1,
        "explanation": "GDP measures the total value of all FINAL goods and services produced WITHIN a country's boundaries in a specific period."
    },
    {
        "question": "Which of the following would be considered an intermediate good?",
        "choices": [
            "Bread sold to a consumer",
            "Flour sold to a bakery",
            "A car sold to a household",
            "A haircut"
        ],
        "correct": 1,
        "explanation": "Flour sold to a bakery is an intermediate good because it's used in further production, not final consumption."
    },
    {
        "question": "The product method of calculating GDP adds up:",
        "choices": [
            "All final goods sold",
            "All incomes generated",
            "Value added by all industries",
            "All consumer expenditures"
        ],
        "correct": 2,
        "explanation": "The product method sums the value added at each stage of production across all industries."
    },
    {
        "question": "Real GDP differs from nominal GDP because:",
        "choices": [
            "It uses current prices",
            "It uses constant prices from a base year",
            "It includes imports",
            "It excludes exports"
        ],
        "correct": 1,
        "explanation": "Real GDP uses constant prices from a base year to eliminate the effect of inflation."
    },
    {
        "question": "If the CPI was 100 in 2020 and 105 in 2021, the inflation rate is:",
        "choices": [
            "5%",
            "105%",
            "0.5%",
            "50%"
        ],
        "correct": 0,
        "explanation": "Inflation rate = (105-100)/100 × 100 = 5%"
    },
    {
        "question": "The labour force consists of:",
        "choices": [
            "Only employed people",
            "Only unemployed people",
            "Employed plus unemployed people",
            "The entire population"
        ],
        "correct": 2,
        "explanation": "Labour force includes both employed and unemployed people who are actively seeking work."
    },
    {
        "question": "GNI equals GDP plus:",
        "choices": [
            "Depreciation",
            "Net income from abroad",
            "Government spending",
            "Taxes"
        ],
        "correct": 1,
        "explanation": "GNI = GDP + Net income from abroad (income earned abroad minus income sent abroad)."
    },
    {
        "question": "In the expenditure method, GDP = C + I + G + ?",
        "choices": [
            "X",
            "M",
            "(X - M)",
            "(M - X)"
        ],
        "correct": 2,
        "explanation": "GDP = C + I + G + (X - M), where (X - M) represents net exports."
    },
    {
        "question": "The base year in an index number always has a value of:",
        "choices": [
            "0",
            "1",
            "10",
            "100"
        ],
        "correct": 3,
        "explanation": "By convention, the base year is assigned a value of 100 in index numbers."
    },
    {
        "question": "Which statement about nominal GDP is TRUE?",
        "choices": [
            "It always accurately reflects economic growth",
            "It can increase even when actual production stays the same",
            "It is adjusted for inflation",
            "It uses base year prices"
        ],
        "correct": 1,
        "explanation": "Nominal GDP can increase due to price increases (inflation) even if actual production remains constant."
    },
    {
        "question": "Depreciation in national accounts refers to:",
        "choices": [
            "Currency losing value",
            "Capital equipment wearing out or becoming obsolete",
            "Stock market decline",
            "Increase in imports"
        ],
        "correct": 1,
        "explanation": "Depreciation is the allowance for capital consumption as equipment wears out or becomes obsolete."
    },
    {
        "question": "If unemployment is 2 million and employment is 28 million, the unemployment rate is:",
        "choices": [
            "7.14%",
            "6.67%",
            "2%",
            "28%"
        ],
        "correct": 1,
        "explanation": "Unemployment rate = 2/(28+2) × 100 = 2/30 × 100 = 6.67%"
    },
    {
        "question": "Double counting in GDP calculation means:",
        "choices": [
            "Counting exports twice",
            "Counting both intermediate and final goods",
            "Counting government spending twice",
            "Measuring GDP twice per year"
        ],
        "correct": 1,
        "explanation": "Double counting occurs when we count the value of intermediate goods plus final goods, overstating GDP."
    },
    {
        "question": "Which is NOT a method of calculating GDP?",
        "choices": [
            "Production method",
            "Income method",
            "Expenditure method",
            "Consumption method"
        ],
        "correct": 3,
        "explanation": "The three methods are: production (value added), income, and expenditure methods."
    }
]

# TEST 2: PUBLIC SECTOR ECONOMICS - PART 1
TEST_2_QUESTIONS = [
    {
        "question": "In a traditional economic system, production decisions are based on:",
        "choices": [
            "Central planning",
            "Market forces",
            "Custom and tradition",
            "Government regulations"
        ],
        "correct": 2,
        "explanation": "Traditional systems rely on customs and traditions passed down through generations."
    },
    {
        "question": "Which economic system is characterized by private ownership and decentralized decision making?",
        "choices": [
            "Command system",
            "Market system",
            "Traditional system",
            "Socialist system"
        ],
        "correct": 1,
        "explanation": "Market systems feature private ownership, individualism, and decentralized decision making."
    },
    {
        "question": "Market failure occurs when:",
        "choices": [
            "Prices are too high",
            "The market cannot achieve efficient allocation of resources",
            "There is too much competition",
            "Government intervenes"
        ],
        "correct": 1,
        "explanation": "Market failure means the market system cannot achieve efficient resource allocation."
    },
    {
        "question": "A monopoly is a market structure with:",
        "choices": [
            "Many firms producing identical products",
            "Few firms with barriers to entry",
            "Only one firm in the industry",
            "Many firms producing differentiated products"
        ],
        "correct": 2,
        "explanation": "A monopoly exists when there is only one firm in the industry."
    },
    {
        "question": "Public goods are characterized by:",
        "choices": [
            "Rivalry and excludability",
            "Non-rivalry and non-excludability",
            "High prices",
            "Private ownership"
        ],
        "correct": 1,
        "explanation": "Public goods are non-rivalrous (one person's use doesn't reduce availability) and non-excludable (can't prevent consumption)."
    },
    {
        "question": "Which of the following is an example of a public good?",
        "choices": [
            "A sandwich",
            "A cinema seat",
            "Street lighting",
            "A museum ticket"
        ],
        "correct": 2,
        "explanation": "Street lighting is a classic public good - it's non-rivalrous and non-excludable."
    },
    {
        "question": "A negative externality is:",
        "choices": [
            "A benefit experienced by society",
            "A cost experienced by society but not by producers/consumers",
            "A government subsidy",
            "A type of tax"
        ],
        "correct": 1,
        "explanation": "Negative externalities are costs imposed on society by producers/consumers who don't bear those costs."
    },
    {
        "question": "Merit goods are goods that:",
        "choices": [
            "People will over-consume",
            "Should be subsidized or provided free",
            "Only wealthy people can afford",
            "Generate negative externalities"
        ],
        "correct": 1,
        "explanation": "Merit goods are beneficial to society and should be subsidized or provided free (like education)."
    },
    {
        "question": "Progressive income taxation means:",
        "choices": [
            "Everyone pays the same tax rate",
            "Lower income earners pay more tax",
            "Higher income earners pay a greater percentage of their income in tax",
            "No one pays tax"
        ],
        "correct": 2,
        "explanation": "Progressive taxation means higher earners pay a higher percentage rate, not just a higher amount."
    },
    {
        "question": "Privatization refers to:",
        "choices": [
            "Government taking over private assets",
            "Selling state-owned assets to the private sector",
            "Creating new public goods",
            "Increasing government spending"
        ],
        "correct": 1,
        "explanation": "Privatization is the sale of state-owned assets to private sector entities."
    },
    {
        "question": "An oligopoly is characterized by:",
        "choices": [
            "One firm only",
            "Many small firms",
            "Few firms with barriers to entry",
            "Perfect competition"
        ],
        "correct": 2,
        "explanation": "Oligopolies have few enough firms that barriers can be erected against new entrants."
    },
    {
        "question": "Which is an example of a positive externality?",
        "choices": [
            "Factory pollution",
            "Traffic congestion",
            "Education creating an informed citizenry",
            "Noise pollution"
        ],
        "correct": 2,
        "explanation": "Education benefits not just the individual but society as a whole - a positive externality."
    },
    {
        "question": "In perfect competition, firms are:",
        "choices": [
            "Price makers",
            "Price takers",
            "Monopolists",
            "Oligopolists"
        ],
        "correct": 1,
        "explanation": "In perfect competition, no single firm can influence market price - they are price takers."
    },
    {
        "question": "A mixed good is:",
        "choices": [
            "Purely public",
            "Purely private",
            "Partially excludable or rivalrous",
            "Always free"
        ],
        "correct": 2,
        "explanation": "Mixed goods have some characteristics of public goods but can be partially excludable or rivalrous."
    },
    {
        "question": "The free-rider problem occurs with:",
        "choices": [
            "Private goods",
            "Public goods",
            "Merit goods",
            "Luxury goods"
        ],
        "correct": 1,
        "explanation": "Public goods suffer from free-rider problems because people can benefit without paying."
    }
]

# TEST 3: PUBLIC SECTOR ECONOMICS - PART 2
TEST_3_QUESTIONS = [
    {
        "question": "Fiscal policy involves:",
        "choices": [
            "Setting interest rates",
            "Controlling money supply",
            "Manipulating government expenditure and tax rates",
            "Regulating banks"
        ],
        "correct": 2,
        "explanation": "Fiscal policy uses government spending and taxation to influence the economy."
    },
    {
        "question": "An expansionary fiscal policy includes:",
        "choices": [
            "Cutting government spending",
            "Raising taxes",
            "Raising government expenditure or reducing taxes",
            "Privatizing state assets"
        ],
        "correct": 2,
        "explanation": "Expansionary policy increases spending or cuts taxes to stimulate the economy."
    },
    {
        "question": "A deflationary fiscal policy would be appropriate to:",
        "choices": [
            "Prevent a recession",
            "Prevent rampant inflation",
            "Increase unemployment",
            "Reduce exports"
        ],
        "correct": 1,
        "explanation": "Deflationary policy (cutting spending/raising taxes) helps cool an overheating economy and control inflation."
    },
    {
        "question": "A budget deficit occurs when:",
        "choices": [
            "Government spending exceeds tax receipts",
            "Tax receipts exceed government spending",
            "Exports exceed imports",
            "GDP is falling"
        ],
        "correct": 0,
        "explanation": "A deficit exists when government spends more than it receives in revenue."
    },
    {
        "question": "A budget surplus occurs when:",
        "choices": [
            "Government spending exceeds revenues",
            "Tax receipts exceed government spending",
            "The economy is in recession",
            "Debt is increasing"
        ],
        "correct": 1,
        "explanation": "A surplus exists when government revenues exceed spending."
    },
    {
        "question": "Capital expenditures include spending on:",
        "choices": [
            "Wages and salaries",
            "Welfare benefits",
            "Roads, hospitals, and schools",
            "Administrative costs"
        ],
        "correct": 2,
        "explanation": "Capital expenditures are investments in long-term assets like infrastructure."
    },
    {
        "question": "Current expenditures include:",
        "choices": [
            "Building new infrastructure",
            "Wages and salaries of public sector staff",
            "Purchasing land",
            "Building hospitals"
        ],
        "correct": 1,
        "explanation": "Current expenditures are recurring operational costs like wages and benefits."
    },
    {
        "question": "Government debt represents:",
        "choices": [
            "Annual deficit",
            "Accumulated deficits over years",
            "Current year spending",
            "Tax receipts"
        ],
        "correct": 1,
        "explanation": "Total debt is the accumulation of all past deficits minus any surpluses."
    },
    {
        "question": "For public finances to be sustainable, the debt-to-GDP ratio should:",
        "choices": [
            "Increase rapidly",
            "Not rise",
            "Double annually",
            "Be eliminated completely"
        ],
        "correct": 1,
        "explanation": "Sustainable finances require the debt-to-GDP ratio to remain stable or decrease."
    },
    {
        "question": "South Africa achieved its first back-to-back primary budget surplus in:",
        "choices": [
            "10 years",
            "12 years",
            "16 years",
            "20 years"
        ],
        "correct": 2,
        "explanation": "South Africa achieved this milestone after 16 years in the 2025 fiscal year."
    },
    {
        "question": "Which best describes the purpose of stabilization policy?",
        "choices": [
            "Eliminate all government debt",
            "Smooth out business cycle fluctuations",
            "Maximize government revenue",
            "Privatize all state assets"
        ],
        "correct": 1,
        "explanation": "Stabilization policy aims to reduce economic fluctuations associated with the business cycle."
    },
    {
        "question": "Primary surplus excludes:",
        "choices": [
            "Tax revenue",
            "Government spending on services",
            "Interest payments on debt",
            "All government expenditure"
        ],
        "correct": 2,
        "explanation": "Primary surplus is revenue minus spending, excluding interest payments."
    },
    {
        "question": "If GDP growth rate exceeds the real interest rate, then:",
        "choices": [
            "Debt grows faster than the economy",
            "Government must run a surplus",
            "Debt shrinks relative to the economy",
            "Fiscal policy is ineffective"
        ],
        "correct": 2,
        "explanation": "When growth exceeds interest rates, debt becomes smaller relative to economic size."
    },
    {
        "question": "Fiscal policy can affect aggregate supply by:",
        "choices": [
            "Only changing consumer demand",
            "Investing in training and infrastructure",
            "Reducing the money supply",
            "Eliminating all taxes"
        ],
        "correct": 1,
        "explanation": "Supply-side fiscal policy includes investments in education, training, and infrastructure."
    },
    {
        "question": "Which is a source of government receipts?",
        "choices": [
            "Budget deficits",
            "Taxes on income and consumption",
            "Government debt",
            "Capital expenditure"
        ],
        "correct": 1,
        "explanation": "Government receipts include taxes, sales, transfers, fines, and investment income."
    }
]

def run_test(test_num: int, questions: List[Dict], test_name: str):
    """Run a single test"""
    clear_screen()
    print_header(f"TEST {test_num}: {test_name}")
    
    print(f"{Colors.CYAN}Welcome to Test {test_num}!{Colors.END}")
    print(f"{Colors.CYAN}This test contains {len(questions)} multiple choice questions.{Colors.END}")
    print(f"{Colors.CYAN}You need 50% to pass (50% = D, 60% = C, 70% = B, 75%+ = A){Colors.END}")
    print(f"{Colors.YELLOW}\nGood luck!{Colors.END}")
    
    input(f"\n{Colors.YELLOW}Press Enter to start the test...{Colors.END}")
    
    score = 0
    total = len(questions)
    
    # Optionally shuffle questions
    test_questions = questions.copy()
    # Uncomment the line below to randomize question order
    # random.shuffle(test_questions)
    
    for i, q in enumerate(test_questions, 1):
        clear_screen()
        print_question(i, total, q["question"])
        
        # Optionally shuffle choices
        choices = q["choices"].copy()
        # Create mapping of shuffled positions to original positions
        original_correct = q["correct"]
        # For simplicity, we're keeping choices in order
        # To shuffle, uncomment below and adjust correct answer tracking
        
        print_choices(choices)
        
        user_answer = get_user_choice(len(choices))
        is_correct = (user_answer - 1) == q["correct"]
        
        if is_correct:
            score += 1
        
        show_result(is_correct, choices[q["correct"]], q["explanation"])
    
    show_final_results(score, total, test_name)
    
    return score, total

def main_menu():
    """Display main menu and handle user selection"""
    while True:
        clear_screen()
        print_header("ECONOMICS 1 QUIZ APPLICATION")
        
        print(f"{Colors.CYAN}{Colors.BOLD}By Sophie Kasse{Colors.END}\n")
        print(f"{Colors.BOLD}Select a test to begin:{Colors.END}\n")
        print(f"  1. Test 1: Measuring Economic Performance ({len(TEST_1_QUESTIONS)} questions)")
        print(f"  2. Test 2: Public Sector Economics - Part 1 ({len(TEST_2_QUESTIONS)} questions)")
        print(f"  3. Test 3: Public Sector Economics - Part 2 ({len(TEST_3_QUESTIONS)} questions)")
        print(f"  4. Take All Tests")
        print(f"  5. Exit")
        
        print(f"\n{Colors.YELLOW}Passing grade: 50% or higher{Colors.END}")
        print(f"{Colors.YELLOW}Grade breakdown: 75%+=A, 70%+=B, 60%+=C, 50%+=D{Colors.END}")
        
        try:
            choice = input(f"\n{Colors.YELLOW}Enter your choice (1-5): {Colors.END}")
            choice = int(choice)
            
            if choice == 1:
                run_test(1, TEST_1_QUESTIONS, "MEASURING ECONOMIC PERFORMANCE")
            elif choice == 2:
                run_test(2, TEST_2_QUESTIONS, "PUBLIC SECTOR ECONOMICS - PART 1")
            elif choice == 3:
                run_test(3, TEST_3_QUESTIONS, "PUBLIC SECTOR ECONOMICS - PART 2")
            elif choice == 4:
                total_score = 0
                total_questions = 0
                
                score1, total1 = run_test(1, TEST_1_QUESTIONS, "MEASURING ECONOMIC PERFORMANCE")
                total_score += score1
                total_questions += total1
                
                score2, total2 = run_test(2, TEST_2_QUESTIONS, "PUBLIC SECTOR ECONOMICS - PART 1")
                total_score += score2
                total_questions += total2
                
                score3, total3 = run_test(3, TEST_3_QUESTIONS, "PUBLIC SECTOR ECONOMICS - PART 2")
                total_score += score3
                total_questions += total3
                
                # Show overall results
                clear_screen()
                print_header("OVERALL RESULTS - ALL TESTS")
                print(f"\n{Colors.BOLD}Test 1 Score: {score1}/{total1} ({(score1/total1)*100:.1f}%){Colors.END}")
                print(f"{Colors.BOLD}Test 2 Score: {score2}/{total2} ({(score2/total2)*100:.1f}%){Colors.END}")
                print(f"{Colors.BOLD}Test 3 Score: {score3}/{total3} ({(score3/total3)*100:.1f}%){Colors.END}")
                print(f"\n{Colors.BOLD}{Colors.CYAN}TOTAL SCORE: {total_score}/{total_questions} ({(total_score/total_questions)*100:.1f}%){Colors.END}")
                
                grade, status = calculate_grade(total_score, total_questions)
                print(f"{Colors.BOLD}Overall Grade: {grade}{Colors.END}")
                
                if status == "PASSED":
                    print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 OVERALL: PASSED! 🎉{Colors.END}")
                else:
                    print(f"\n{Colors.RED}{Colors.BOLD}OVERALL: NOT PASSED{Colors.END}")
                
                input(f"\n{Colors.YELLOW}Press Enter to return to main menu...{Colors.END}")
                
            elif choice == 5:
                clear_screen()
                print(f"\n{Colors.GREEN}Thank you for using the Economics 1 Quiz Application!{Colors.END}")
                print(f"{Colors.CYAN}Keep studying and good luck with your exams!{Colors.END}\n")
                break
            else:
                print(f"{Colors.RED}Please enter a number between 1 and 5{Colors.END}")
                input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
                
        except ValueError:
            print(f"{Colors.RED}Please enter a valid number{Colors.END}")
            input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        except KeyboardInterrupt:
            clear_screen()
            print(f"\n{Colors.GREEN}Thank you for using the Economics 1 Quiz Application!{Colors.END}\n")
            break

if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"\n{Colors.RED}An error occurred: {e}{Colors.END}")
        print(f"{Colors.YELLOW}Please report this issue.{Colors.END}\n")
