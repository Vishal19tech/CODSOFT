def quiz():
    print("******Welcome to QUIZ-O-MANIA******\n Rules :\n a) This quiz have 10 questions.\n b) Each question have four options.\n c) Each right answer gives you 5 points and wrong answer deducts 2 points. \n Score Criteria :\n - Score more than 40 points to get 'A' Grade\n - Score more than 30 points to get 'B' Grade\n - Score more than 20 points to get 'C' Grade\n - Score more than 10 points to get 'D' Grade\n - If you scored less than 10 point you get 'E' Grade " )
    q1 = "Which god is also known as 'Gauri Nandan'?"
    q1o1 = "a) Agni"
    q1o2 = "b) Indra"
    q1o3 = "c) Hanuman"
    q1o4 = "d) Ganesh"
    q1_options = [q1o1, q1o2, q1o3, q1o4]
    print(q1)
    for i in q1_options:
        print(i)
    ans1 = input("Enter Your Answer :")
    points = 0
    while ans1 == "GANESH" or ans1 == "Ganesh" or ans1 == "ganesh" or ans1 == "d" or ans1 == "D":
        print("Correct Answer you get 5 points")
        points = points + 5
        print(f"You have {points} points")
        break
    else:
        print("Wrong Answer, Correct answer is Ganesh")
        points = points - 2
        print(f"You have {points} points")

    q2 = "Which city is known as Pink City in India ?"
    q2o1 = "a) Delhi"
    q2o2 = "b) Jaipur"
    q2o3 = "c) Mumbai"
    q2o4 = "d) Kochi"
    q2_options = [q2o1, q2o2, q2o3, q2o4]
    print(q2)
    for i in q2_options:
        print(i)
    ans2 = input("Enter Your Answer :")
    while ans2 == "JAIPUR" or ans2 == "jaipur" or ans2 == "Jaipur" or ans2 == "b" or ans2 == "B":
        print("Correct Answer you get 5 points")
        points = points + 5
        print(f"You have {points} points")
        break
    else:
        print("Wrong Answer, Correct answer is Jaipur")
        points = points - 2
        print(f"You have {points} points")

    q3 = "Which city is known as the 'Silicon Valley Of India'?"
    q3o1 = "a) Delhi"
    q3o2 = "b) Jaipur"
    q3o3 = "c) Mumbai"
    q3o4 = "d) Bangalore"
    q3_options = [q3o1, q3o2, q3o3, q3o4]
    print(q3)
    for i in q3_options:
        print(i)
    ans3 = input("Enter Your Answer :")
    while ans3 == "Bangalore" or ans3 == "bangalore" or ans3 == "BANGALORE" or ans3 == "d" or ans3 == "D":
        print("Correct Answer you get 5 points")
        points = points + 5
        print(f"You have {points} points")
        break
    else:
        print("Wrong Answer, Correct answer is Bangalore")
        points = points - 2
        print(f"You have {points} points")

    q4 = "Which city is known as the 'City of Temples'?"
    q4o1 = "a) Delhi"
    q4o2 = "b) Varanasi"
    q4o3 = "c) Surat"
    q4o4 = "d) Gaya"
    q4_options = [q4o1, q4o2, q4o3, q4o4]
    print(q4)
    for i in q4_options:
        print(i)
    ans4 = input("Enter Your Answer :")
    while ans4 == "Varanasi" or ans4 == "varanasi" or ans4 == "VARANASI" or ans4 == "b" or ans4 == "B":
        print("Correct Answer you get 5 points")
        points = points + 5
        print(f"You have {points} points")
        break
    else:
        print("Wrong Answer, Correct answer is Varanasi")
        points = points - 2
        print(f"You have {points} points")


    q5 = "Which city is known as the 'City of Oranges'?"
    q5o1 = "a) Nagpur"
    q5o2 = "b) Bhopal"
    q5o3 = "c) Surat"
    q5o4 = "d) Ranchi"
    q5_options = [q5o1, q5o2, q5o3, q5o4]
    print(q5)
    for i in q5_options:
        print(i)
    ans5 = input("Enter Your Answer :")
    while ans5 == "Nagpur" or ans5 == "NAGPUR" or ans5 == "nagpur" or ans5 == "A" or ans5 == "a":
        print("Correct Answer you get 5 points")
        points = points + 5
        print(f"You have {points} points")
        break
    else:
        print("Wrong Answer, Correct answer is Nagpur")
        points = points - 2
        print(f"You have {points} points")

    q6 = "Which city is known as the 'City of Festivals'?"
    q6o1 = "a) Kochi"
    q6o2 = "b) Madurai"
    q6o3 = "c) Delhi"
    q6o4 = "d) Vellore"
    q6_options = [q6o1, q6o2, q6o3, q6o4]
    print(q6)
    for i in q6_options:
        print(i)
    ans6 = input("Enter Your Answer :")
    while ans6 == "Madurai" or ans6 == "madurai" or ans6 == "MADURAI" or ans6 == "b" or ans6 == "B":
        print("Correct Answer you get 5 points")
        points = points + 5
        print(f"You have {points} points")
        break
    else:
        print("Wrong Answer, Correct answer is Maurai")
        points = points - 2
        print(f"You have {points} points")

    q7 = "Which city is known as the 'City of Pearls'?"
    q7o1 = "a) Kochi"
    q7o2 = "b) Lucknow"
    q7o3 = "c) Chandigarh"
    q7o4 = "d) Hyderabad"
    q7_options = [q7o1, q7o2, q7o3, q7o4]
    print(q7)
    for i in q7_options:
        print(i)
    ans7 = input("Enter Your Answer :")
    while ans7 == "Hyderabad" or ans7 == "hyderabad" or ans7 == "HYDERABAD" or ans7 == "D" or ans7 == "d":
        print("Correct Answer you get 5 points")
        points = points + 5
        print(f"You have {points} points")
        break
    else:
        print("Wrong Answer, Correct answer is Hyderabad")
        points = points - 2
        print(f"You have {points} points")

    q8 = "Which city is known as the 'City of Weavers'?"
    q8o1 = "a) Kanpur"
    q8o2 = "b) Panipat"
    q8o3 = "c) Kolhapur"
    q8o4 = "d) Jaipur"
    q8_options = [q8o1, q8o2, q8o3, q8o4]
    print(q8)
    for i in q8_options:
        print(i)
    ans8 = input("Enter Your Answer :")
    while ans8 == "Panipat" or ans8 == "PANIPAT" or ans8 == "panipat" or ans8 == "b" or ans8 == "B":
        print("Correct Answer you get 5 points")
        points = points + 5
        print(f"You have {points} points")
        break
    else:
        print("Wrong Answer, Correct answer is Panipat")
        points = points - 2
        print(f"You have {points} points")

    q9 = "Which city is known as the 'Leather City'?"
    q9o1 = "a) Kanpur"
    q9o2 = "b) Hyderabad"
    q9o3 = "c) Gaya"
    q9o4 = "d) Chandigarh"
    q9_options = [q9o1, q9o2, q9o3, q9o4]
    print(q9)
    for i in q9_options:
        print(i)
    ans9 = input("Enter Your Answer :")
    while ans9 == "Kanpur" or ans9 == "KANPUR" or ans9 == "kanpur" or ans9 == "a" or ans9 == "A":
        print("Correct Answer you get 5 points")
        points = points + 5
        print(f"You have {points} points")
        break
    else:
        print("Wrong Answer, Correct answer is Kanpur")
        points = points - 2
        print(f"You have {points} points")

    q10 = "Which city is known as the 'Queen of Arabian Sea'?"
    q10o1 = "a) Kochi"
    q10o2 = "b) Madurai"
    q10o3 = "c) Chennai"
    q10o4 = "d) Vellore"
    q10_options = [q10o1, q10o2, q10o3, q10o4]
    print(q10)
    for i in q10_options:
        print(i)
    ans10 = input("Enter Your Answer :")
    while ans10 == "Kochi" or ans10 == "KOCHI" or ans10 == "kochi" or ans10 == "A" or ans10 == "a":
        print("Correct Answer you get 5 points")
        points = points + 5
        print(f"You Scored {points} points")
        break
    else:
        print("Wrong Answer, Correct answer is Kochi")
        points = points - 2
        print(f" You Scored {points} points")

    if points >= 40:
        print("Congratualtions! You got 'A' Grade.")
    elif points >= 30:
        print("Congratualtions! You got 'B' Grade.")
    elif points >=20:
        print("You got 'C' Grade.")
    elif points >=10:
        print("You got 'D' Grade.")
    else:
        print("It seems bad, You got 'E' Grade.")

    print("****Thank you for playing Quiz-O-Mania****")

    play_again = input("DO YOU WANT TO PLAY AGAIN, TYPE Y for YES and N for NO :")
    if play_again == "Y" or play_again == "y":
        return quiz()
    else:
        print("I hope you enjoyed it!")

quiz()