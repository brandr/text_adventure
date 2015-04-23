import random

TEXT = "text"
NEXT = "next"
CHANCE = "chance"
OPTIONS = "options"
ACTIONS = "actions"
BABY_VERSION = "baby_version"

# action contstants

GAME_OVER = "game_over"
INCREASE_DAYS = "increase_days"
INCREASE_SCORE = "increase_score"
INCREASE_BABIES = "increase_babies"
INCREASE_BABIES_RESPECT = "increase_babies_respect"

# special event key names

LOSE_ALL_BABIES_RESPECT = "lose_all_babies_respect"

# event key names

START = "start"
SNAKE_POISON_DEATH = "snake_poison_death"
UNEVENTFUL_NIGHT_1 = "uneventful_night_1"
SNAKE_FLEE = "snake_flee"
MORNING_HUNGER_1 = "morning_hunger_1"
MORNING_HUNGER_2 = "morning_hunger_2"
SWIMMING_URGE = "swimming_urge"
WATER_CHOW = "water_chow"
TREE_LAND_NO_FOOD = "tree_land_no_food"
TREE_LAND_NO_FOOD_CONTINUED = "tree_land_no_food_continued"
RIGHT_WHERE_I_AM_NOTHING = "right_where_I_am_nothing"
UNEVENTFUL_WAIT_1 = "uneventful_wait_1"
MALLARD_FLYING_OVERHEAD = "mallard_flying_overhead"
GO_SWIMMING_1 = "go_swimming_1"
RETURN_TO_LAND = "return_to_land"
MALLARD_COURTING_1	= "mallard_courting_1"
MALLARD_COURTING_CHOICE_1 = "mallard_courting_choice_1"
FAILED_COURTING_RESPONSE_1 = "failed_courting_response_1"
MALLARD_COURTING_GIVEUP_1 = "mallard_courting_giveup_1"
COURTING_SUCCESS_1 = "courting_success_1"
DONT_GO_SWIMMING = "dont_go_swimming"
GO_FLYING_1 = "go_flying_1"
UNEVENTFUL_DAY_1 = "uneventful_day_1"
UNEVENTFUL_NIGHT_2 = "uneventful_night_2"
WAKE_UP_SNAKE = "wake_up_snake"
SNAKE_IDENTIFY	= "snake_identify"
SNAKE_POISON_DEATH_2 = "snake_poison_death_2"
RETURN_TO_LAND_2 = "return_to_land_2"
TOUCAN_ENCOUNTER = "touncan_encounter"
TOUCAN_SEE = "toucan_see"
TOUCANT = "toucant"
JAGUAR_ENCOUNTER = "jaguar_encounter"
UNEVENTFUL_NIGHT_3 = "uneventful_night_3"
JAGUAR_WADDLE_DEATH = "jaguar_waddle_death"
JAGUAR_SWIMMING_DEATH = "jaguar_swimming_death"
JAGAUR_ESCAPE = "jaguar_escape"
GETTING_LATE = "getting_late"
MORNING_ENCOUNTER_1 = "morning_encounter_1"
DUCK_HUNTER_DEATH = "duck_hunter_death"
BAD_AIM	= "bad_aim"
DUCK_HUNTER_SEE = "duck_hunter_see"
FEMALE_DUCK_ENCOUNTER = "female_duck_encounter"
FAIL_CHASE_DUCK = "fail_chase_duck"
NEST_DISCOVER = "nest_discover"
EGG_THIEF = "egg_thief"
GOOD_DUCK = "good_duck"
DUCK_BEFRIEND_FAIL = "duck_befriend_fail"
NEST_SITTING_1 = "nest_sitting_1"
NEST_SITTING_2 = "nest_sitting_2"
KEEP_SITTING_1 = "keep_sitting_1"
HEARTLESS_MOTHER = "heartless_mother"
EXTREME_HUNGER = "extreme_hunger"
EGGS_EATEN = "eggs_eaten"
STILL_SITTING_1 = "still_sitting_1"
STILL_SITTING_2 = "still_sitting_2"
STILL_SITTING_3 = "still_sitting_3"
MALLARD_SCARED = "mallard_scared"
MORE_MALLARDS_FLYING = "more_mallards_flying"
GOOD_CHOICE = "good_choice"
GOOD_FATHER = "good_father"
INJURED_DADDY = "injured_daddy"
EASY_EGGSITTING = "easy_eggsitting"
SO_CUTE = "so_cute"
BABIES_FED = "babies_fed"
HUNGRY_BABIES = "hungry_babies"
WOW_JUST_WOW = "wow_just_wow"
BABIES_DONT_WANT_IT = "babies_dont_want_it"
SATISFIED_BABIES = "satisfied_babies"
HUNGRY_BABIES_2 = "hungry_babies_2"
NOT_HUNGRY = "not_hungry"
SNUGGLING_BABIES = "snuggling_babies"
SLEEPING_BABIES = "sleeping_babies"
SAFE_SLEEPY_BABIES = "safe_sleepy_babies"
BABY_INJURED = "baby_injured"
BABY_RECOVERY = "baby_recovery"
BABY_FATALITY = "baby_fatality"
BABY_EATEN = "baby_eaten"
SWIMMING_BABIES_SHORE = "swimming_babies_shore"
SWIMMING_BABIES = "swimming_babies"
DISAPPOINTED_BABIES = "disappointed_babies"
DONE_SWIMMING = "done_swimming"
TURTLE_LOG = "turtle_log"
JUST_A_LOG = "just_a_log"
JUST_A_LOG_ANNOYED_BABIES = "just_a_log_annoyed_babies"
TURTLE_ATTACK = "turtle_attack"
TURTLE_ATTACK_FAIL = "turtle_attack_fail"
FAILED_TURTLE_SCHEME = "failed_turtle_scheme"
EVENTFUL_NIGHT_1 = "eventful_night_1"

MASTER_DIALOG_DATA_MAP = {

	# special events

	LOSE_ALL_BABIES_RESPECT:{
		TEXT:[
			"Your babies hate you and abandoned you and disappeared into the jungle,",
			"and have probably been eaten by now.",
			"GAME OVER"
		],
		ACTIONS:[
			(GAME_OVER, 0)
		]
	},

	# events

	START:{
		TEXT:[
		"You are a female duck in a tropical rainforest.", 
		"Your job, as with all ducks, is to procreate and survive as long as possible.", 
		"Click the arrow keys to choose various options for events, and enter to make your choice.",
		"Now, here is your first event:", 
		"", 
		"You come across a hollowed tree that seems like it would be a decent place to spend the night."
		],
		OPTIONS:[
			{TEXT:"stay the night", NEXT:SNAKE_POISON_DEATH},
			{TEXT:"spend the night on the rainforest floor", NEXT:UNEVENTFUL_NIGHT_1}, #+
			{TEXT:"quack uncontrollably", NEXT:SNAKE_FLEE}	#+
		]
	},
	SNAKE_POISON_DEATH:{
		TEXT:[
			"You decide to stay the night, but just before you go into the tree trunk,", 
			"a snake bursts out of the trunk and poisons you.", 
			"GAME OVER."
		],
		ACTIONS:[
			(GAME_OVER, None)
		]
	},
	UNEVENTFUL_NIGHT_1:{
		TEXT:[
			"You spend the night on the rainforest floor and have an uneventful night. Time to start the day!"
		],
		ACTIONS:[
			(INCREASE_DAYS, 1),
			(INCREASE_SCORE, 1)
			],
		CHANCE:[(.5, MORNING_HUNGER_1),(.3, SWIMMING_URGE), (.2, WAKE_UP_SNAKE)]	
	},
	MORNING_HUNGER_1:{
		TEXT:[
			"You feel rather hungry and decide to go out looking for a snack. Where do you look?"
		],
		OPTIONS:[
			{TEXT:"On the water", NEXT:WATER_CHOW},	#-
			{TEXT:"In a tree", NEXT:TREE_LAND_NO_FOOD},
			{TEXT:"Right where I am", NEXT:RIGHT_WHERE_I_AM_NOTHING}
		],
		BABY_VERSION:{
			TEXT:[
				"Your babies are hungry. What do you feed them?"
			],
			OPTIONS:[
				{TEXT:"Nothing", NEXT:HUNGRY_BABIES_2},
				{TEXT:"A dead crow", NEXT:BABIES_DONT_WANT_IT},
				{TEXT:"A frog you caught", CHANCE:[(.6, BABIES_DONT_WANT_IT),(.4, SATISFIED_BABIES)]},
				{TEXT:"Various grasses", CHANCE:[(.3, BABIES_DONT_WANT_IT),(.7, SATISFIED_BABIES)]},
				{TEXT:"Some berries", CHANCE:[(.5, BABIES_DONT_WANT_IT),(.5, SATISFIED_BABIES)]},
				{TEXT:"A snail", CHANCE:[(.5, BABIES_DONT_WANT_IT),(.5, SATISFIED_BABIES)]},
				{TEXT:"A mango", NEXT:BABIES_DONT_WANT_IT},
			]
		}
	},
	SATISFIED_BABIES:{	
		TEXT:[
			"Your babies seem to be in the mood for that, and they gladly eat it."
		],
		ACTIONS:[
			(INCREASE_BABIES_RESPECT, 1)
		],
		CHANCE:[(.7, SWIMMING_URGE), (.1, SNUGGLING_BABIES), (.2, SLEEPING_BABIES)]
	},
	BABIES_DONT_WANT_IT:{
		TEXT:[
			"Mmm, no, your babies don't want to eat that."
		],
		ACTIONS:[
			(INCREASE_BABIES_RESPECT, -2)
		],
		NEXT:MORNING_HUNGER_1
	},
	HUNGRY_BABIES_2:{
		TEXT:[
			"You don't feed your babies and they get very hungry and upset with you."
		],
		ACTIONS:[
			(INCREASE_BABIES_RESPECT, -20)
		],
		NEXT:MORNING_HUNGER_1
	},
	SNUGGLING_BABIES:{
		TEXT:[
			"Your babies all start to huddle together around you for warmth."
		],
		ACTIONS:[
			(INCREASE_BABIES_RESPECT, 1)
		],
		NEXT:UNEVENTFUL_NIGHT_1
	},
	SLEEPING_BABIES:{
		TEXT:[
			"Your babies seem tired and head back to the nest to sleep."
		],
		OPTIONS:[
			{TEXT:"Go get myself some food. I'm hungry", CHANCE:[(.9, NOT_HUNGRY), (.1, BABY_INJURED)]},
			{TEXT:"Go back to the nest with them", NEXT:SAFE_SLEEPY_BABIES},
			{TEXT:"Go get some food for them", NEXT:GETTING_LATE}
		]
	},
	SAFE_SLEEPY_BABIES:{
		TEXT:[
			"You go back to the nest and make sure your babies are safe."
		],
		NEXT:UNEVENTFUL_NIGHT_2
	},
	NOT_HUNGRY:{
		TEXT:[
			"You go get yourself some food and return back to your nest.",
			"Your babies are okay."
		],
		NEXT:UNEVENTFUL_NIGHT_1
	},
	BABY_INJURED:{
		TEXT:[
			"After you get back to the nest, you see that one of your babies hurt himself on a sharp rock.",
		],
		OPTIONS:[
			{TEXT:"Help him", CHANCE:[(.6, BABY_RECOVERY), (.1, BABY_EATEN), (.3, BABY_FATALITY)]}
		]
	},
	BABY_RECOVERY:{
		TEXT:[
			"Your baby doesn't appear to be bleeding and you manage to make sure he's okay."
		],
		ACTIONS:[
			(INCREASE_BABIES_RESPECT, 2)
		],
		NEXT:GETTING_LATE
	},
	BABY_EATEN:{
		TEXT:[
			"You try to help your chick, but some sort of wild lizard snatches it up."
		],
		ACTIONS:[
			(INCREASE_BABIES, -1),
			(INCREASE_BABIES_RESPECT, -30)
		],
		NEXT:GETTING_LATE
	},
	BABY_FATALITY:{
		TEXT:[
			"You try and help your baby, but eventually his wing is punctured and he dies of blood loss."
		],
		ACTIONS:[
			(INCREASE_BABIES, -1),
			(INCREASE_BABIES_RESPECT, -10)
		],
		NEXT:GETTING_LATE
	},
	WATER_CHOW:{	
		TEXT:[
			"You find some good eats on the water and are no longer hungry."
		],
		NEXT:RETURN_TO_LAND
	},
	TREE_LAND_NO_FOOD:{
		TEXT:[
			"You land on a tree but don't find any food a duck would care about on it."
		],
		OPTIONS:[
			{TEXT:"Land on another tree!", NEXT:TREE_LAND_NO_FOOD},
			{TEXT:"Fly off the tree", NEXT:MORNING_HUNGER_2},
			{TEXT:"Wait", CHANCE:[(.9, UNEVENTFUL_WAIT_1), (.1, MALLARD_FLYING_OVERHEAD)]} 
		]
	},
	TREE_LAND_NO_FOOD_CONTINUED:{
		TEXT:[
			"You're still on the tree. What do you do?"
		],
		OPTIONS:[
			{TEXT:"Land on another tree!", NEXT:TREE_LAND_NO_FOOD},
			{TEXT:"Fly off the tree", NEXT:MORNING_HUNGER_2},
			{TEXT:"Wait", CHANCE:[(.9, UNEVENTFUL_WAIT_1), (.1, MALLARD_FLYING_OVERHEAD)]} 
		]
	},
	UNEVENTFUL_WAIT_1:{
		TEXT:[
			"You wait, but nothing eventful happens."
		],
		NEXT:TREE_LAND_NO_FOOD_CONTINUED
	},
	MALLARD_FLYING_OVERHEAD:{	
		TEXT:[
			"You see what appears to be a mallard flying overhead."
		],
		OPTIONS:[
			{TEXT:"Ignore him", NEXT:MORE_MALLARDS_FLYING},
			{TEXT:"Fly up to him", NEXT:COURTING_SUCCESS_1},
			{TEXT:"Alert him to nonexistent danger", NEXT:MALLARD_SCARED}
		]
	},
	MORE_MALLARDS_FLYING:{
		TEXT:[
			"You decide to wait it out and eventually five mallards are now circling overhead.",
			"You believe this is a courting ritual. Which one will you choose?"
		],
		OPTIONS:[
			{TEXT:"The handsomest one", NEXT:GOOD_CHOICE},
			{TEXT:"The friendliest one", NEXT:GOOD_CHOICE},
			{TEXT:"The first one", NEXT:GOOD_CHOICE},
			{TEXT:"The strongest-looking one", NEXT:GOOD_CHOICE},
			{TEXT:"The abnormal-looking one", NEXT:INJURED_DADDY}
		]
	},
	GOOD_CHOICE:{
		TEXT:[
			"Good choice! That seems like a good and healthy duck."
		],
		NEXT:COURTING_SUCCESS_1
	},
	INJURED_DADDY:{
		TEXT:[
			"You fly up and try and court the abnormal-looking one and then see that he's injured.",
			"Do you still choose him?"
		],
		OPTIONS:[
			{TEXT:"Yes", NEXT:GOOD_FATHER},
			{TEXT:"No", NEXT:GETTING_LATE}
		]
	},
	GOOD_FATHER:{
		TEXT:[
			"You choose and successfully court the injured mallard, and it turns out that he made a good father,", 
			"because his wing was kind of broken, and so he couldn't fly away."
		],
		NEXT:EASY_EGGSITTING
	},
	EASY_EGGSITTING:{
		TEXT:[
			"Eventually, you lay a nice crop of four eggs and the father of the eggs goes and gets you some food,",
			"and so it's pretty easy eggsitting."
		],
		ACTIONS:[
			(INCREASE_SCORE, 97),
			(INCREASE_DAYS, 97)
		],
		NEXT:STILL_SITTING_3
	},
	MALLARD_SCARED:{
		TEXT:[
			"You alert the mallard to danger (that doesn't exist) and the mallard flies away hastily."
		],
		NEXT:GETTING_LATE
	},
	MORNING_HUNGER_2:{
		TEXT:[
			"You decide to fly off the tree, but you didn't find any food", "Where do you look for food?"
		],
		OPTIONS:[
			{TEXT:"On the water", NEXT:WATER_CHOW}
		]
	},
	RIGHT_WHERE_I_AM_NOTHING:{	#X
		TEXT:[
			"You don't find anything edible of interest."
		],
	},
	SWIMMING_URGE:{
		TEXT:[
			"You feel a strong urge to go swimming."
		],
		OPTIONS:[
			{TEXT:"Go swimming", NEXT:GO_SWIMMING_1},
			{TEXT:"Don't go swimming", NEXT:DONT_GO_SWIMMING},
			{TEXT:"Go flying", NEXT:GO_FLYING_1} 
		],
		BABY_VERSION:{ #/
			TEXT:[
				"Your babies want to go swimming in a nearby pond."
			],
			OPTIONS:[
				{TEXT:"Let them, and stay on shore", NEXT:SWIMMING_BABIES_SHORE},
				{TEXT:"Let them, and swim with them", NEXT:SWIMMING_BABIES},
				{TEXT:"Don't let them", NEXT:DISAPPOINTED_BABIES}
			]
		}
	},
	SWIMMING_BABIES_SHORE:{ #/
		TEXT:[
			"You are getting some nice sun and your babies are swimming happily."
		],	
		ACTIONS:[
			(INCREASE_BABIES_RESPECT, 3)
		],
		CHANCE:[(.6, TURTLE_LOG), (.4, DONE_SWIMMING) ]
	},
	TURTLE_LOG:{ #/
		TEXT:[
			"You see what looks to be either a small log or a snapping turtle in the water close to your babies."
		],
		OPTIONS:[
			{TEXT:"Let the babies be", CHANCE:[(.8, JUST_A_LOG), (.1, TURTLE_ATTACK), (.1, TURTLE_ATTACK_FAIL)]},
			{TEXT:"Tell them to get out", CHANCE:[(.8, JUST_A_LOG_ANNOYED_BABIES), (.2, FAILED_TURTLE_SCHEME)]}
		]
	},
	JUST_A_LOG:{
		TEXT:[
			"Phew! It was just a log."
		],
		NEXT:DONE_SWIMMING
	},
	JUST_A_LOG_ANNOYED_BABIES:{
		TEXT:[
			"Your babies get out of the water, but are confused and annoyed as to why they had to get out,",
			"because it was just a log."
		],
		ACTIONS:[
			(INCREASE_BABIES_RESPECT, -5)
		],
		NEXT:GETTING_LATE
	},
	TURTLE_ATTACK:{
		TEXT:[
			"You let them be, but then you see that it actually was a turtle, and the turtle drags",
			"one of your chicks down into the pond."
		],
		ACTIONS:[
			(INCREASE_BABIES, -1),
			(INCREASE_BABIES_RESPECT, -15)
		],
		NEXT:GETTING_LATE
	},
	TURTLE_ATTACK_FAIL:{
		TEXT:[
			"You see that it actually was a turtle, and it tries to kill one of your duclkings, but luckily fails."
		],
		ACTIONS:[
			(INCREASE_BABIES_RESPECT, -10)
		],
		NEXT:GETTING_LATE
	},
	FAILED_TURTLE_SCHEME:{
		TEXT:[
			"The babies get out of the water just before you realize it actually was a turtle,",
			"but now your babies are safe."
		],
		ACTIONS:[
			(INCREASE_BABIES_RESPECT, 25)
		],
		NEXT:GETTING_LATE
	},
	DONE_SWIMMING:{
		TEXT:[
			"After a few hours, your babies are done swimming and go back to the nest."
		],
		NEXT:GETTING_LATE
	},
	SWIMMING_BABIES:{
		TEXT:[
			"You have a marvelous time swimming with your babies."
		],
		ACTIONS:[
			(INCREASE_BABIES_RESPECT, 5)
		],
		NEXT:EVENTFUL_NIGHT_1
	},
	DISAPPOINTED_BABIES:{
		TEXT:[
			"You don't let them, and your babies are disappointed."
		],
		ACTIONS:[
			(INCREASE_BABIES_RESPECT, -5)
		],
		NEXT:MORNING_HUNGER_1
	},
	DONT_GO_SWIMMING:{
		TEXT:[
		"You decide not to go swimming, but then you realize you're hungry.", "Where do you look for food?"
		],
		OPTIONS:[
			{TEXT:"On the water", NEXT:WATER_CHOW},	
			{TEXT:"In a tree", NEXT:TREE_LAND_NO_FOOD},
			{TEXT:"Right where I am", NEXT:RIGHT_WHERE_I_AM_NOTHING}
		]
	},
	EVENTFUL_NIGHT_1:{
		TEXT:[
			"In the middle of the night, you see a duck hunter and you manage to keep your babies safe,",
			"but it was due to your poor judgement that one of their wings was hurt."
		],
		ACTIONS:[
			(INCREASE_BABIES_RESPECT, -10)
		],
		CHANCE:[(.1, JAGUAR_ENCOUNTER), (.2, WAKE_UP_SNAKE), (.6, MORNING_HUNGER_1), (.1, SWIMMING_URGE)]
	},
	GO_FLYING_1:{
		TEXT: [
			"You decide that it's best to not go swimming (for some reason), and instead go flying to ease your nerves."
		],
		NEXT:RETURN_TO_LAND
	},
	GO_SWIMMING_1:{
		TEXT:[
			"You decide to go swimming to ease your nerves."
		],
		OPTIONS:[
			{TEXT:"Keep swimming", NEXT:MALLARD_COURTING_1},
			{TEXT:"Go back on land", CHANCE:[(.4, MORNING_HUNGER_2), (.6, RETURN_TO_LAND)]}	#/
		]
	},
	MALLARD_COURTING_1:{	
		TEXT:[
			"You see a mallard swimming beside you and he is bobbing his beak up and down in the water."
		],
		OPTIONS:[
			{TEXT:"Swim away", NEXT:RETURN_TO_LAND},
			{TEXT:"Fly away", NEXT:RETURN_TO_LAND},
			{TEXT:"Ignore him", NEXT:MALLARD_COURTING_CHOICE_1}
		]
	},
	MALLARD_COURTING_CHOICE_1:{
		TEXT:[
			"The mallard is still swimming beside you and you believe he is trying to court you.", "What do you do?"
		],
		OPTIONS:[
			{TEXT:"FLY AWAY!!", NEXT:RETURN_TO_LAND},
			{TEXT:"Fly over him and get some food from the water and give it to him.", NEXT:FAILED_COURTING_RESPONSE_1},
			{TEXT:"Keep ignoring him", NEXT:MALLARD_COURTING_GIVEUP_1},
			{TEXT:"Bob your bill up and down and then bow to him.", NEXT:COURTING_SUCCESS_1}
		]
	},
	FAILED_COURTING_RESPONSE_1:{
		TEXT:[
			"The mallard is confused by your unusual courting methods and eventually gives up."
		],
		NEXT:GETTING_LATE
	},
	MALLARD_COURTING_GIVEUP_1:{
		TEXT:[
			"The mallard is eventually discouraged and flies away."
		],
		NEXT:GETTING_LATE
	},
	COURTING_SUCCESS_1:{
		TEXT:[
			"Huzzah! You successfully courted the mallard and commence \"private activities\"."
		],
		NEXT:NEST_SITTING_2
	},
	RETURN_TO_LAND:{
		TEXT:[
			"You return to land feeling refreshed."
		],
		CHANCE:[(.2, TOUCAN_ENCOUNTER), (.1, JAGUAR_ENCOUNTER), (.5, UNEVENTFUL_DAY_1), (.2, FEMALE_DUCK_ENCOUNTER)]
	},
	TOUCAN_ENCOUNTER:{	#-
		TEXT:[
			"You encounter a brightly colored bird, but it doesn't appear to be a duck."
		],
		OPTIONS:[
			{TEXT:"Fly away", NEXT:RETURN_TO_LAND_2},
			{TEXT:"Get a closer look", NEXT:TOUCAN_SEE},
			{TEXT:"Ignore it", NEXT:TOUCANT}
		]
	},
	TOUCAN_SEE:{
		TEXT:[
			"You go for a closer look and eventually realize that it's a toucan and then walk past it."
		],
		NEXT:UNEVENTFUL_DAY_1
	},
	TOUCANT:{	#-
		TEXT:[
			"You ignore it and have an otherwise uneventful day."
		],
		NEXT:UNEVENTFUL_NIGHT_3
	},
	JAGUAR_ENCOUNTER:{	#-
		TEXT:[
			"JAGUAR!!!!!"
		],
		OPTIONS:[
			{TEXT:"RUN!!", NEXT:JAGUAR_WADDLE_DEATH},
			{TEXT:"FLY!!", NEXT:JAGAUR_ESCAPE},
			{TEXT:"SWIM!!", NEXT:JAGUAR_SWIMMING_DEATH}
		]
	},
	JAGUAR_WADDLE_DEATH:{
		TEXT:[
			"You stupid duck! Ducks can only waddle at two or three miles per hour!", "GAME OVER"
		],
		ACTIONS:[
			(GAME_OVER, None)
		]
	},
	JAGUAR_SWIMMING_DEATH:{
		TEXT:[
			"You stupid duck! Jaguars are one of the few swimming cats!", "GAME OVER"
		],
		ACTIONS:[
			(GAME_OVER, None)
		]	
	},
	JAGAUR_ESCAPE:{
		TEXT:[
			"Phew! That was a close one! Lucky jaguars can't fly, am I right?"
		],
		NEXT:GETTING_LATE
	},
	FEMALE_DUCK_ENCOUNTER:{
		TEXT:[
			"You encounter another female duck."
		],
		OPTIONS:[
			{TEXT:"Chase it away", CHANCE:[(.7, FAIL_CHASE_DUCK), (.3, NEST_DISCOVER)]},
			{TEXT:"Try and befriend it", NEXT:DUCK_BEFRIEND_FAIL},
			{TEXT:"Ignore it", NEXT:UNEVENTFUL_DAY_1}
		]
	},
	FAIL_CHASE_DUCK:{
		TEXT:[
			"You quack violently at the other female duck, but it seems unscathed by your quacking and",
			"quacks back even louder at you. It seems to be sitting on a nest."
		],
		NEXT:GETTING_LATE
	},
	NEST_DISCOVER:{ #-
		TEXT:[
			"You chase the duck away and discover it was sitting on a nest with eggs in it."
		],
		OPTIONS:[
			{TEXT:"I don't need to lay the eggs to be the mother!", NEXT:EGG_THIEF},
			{TEXT:"Leave them be. They're not my babies.", NEXT:GETTING_LATE},
			{TEXT:"Oh, no! I better get these eggs back to the mother!", NEXT:GOOD_DUCK}
		]
	},
	EGG_THIEF:{
		TEXT:[
			"Wow, I'm not sure I like you anymore.", "You know what?", "You can have the eggs, but score -50!"
		],
		ACTIONS:[
			(INCREASE_SCORE, -50)
		],
		NEXT:NEST_SITTING_1
	},
	GOOD_DUCK:{
		TEXT:[
			"You spend the rest of the night trying to find the mother of those eggs and eventulaly find her, ", 
			"and give her back her eggs.", 
			"Score +5"
		],
		ACTIONS:[
			(INCREASE_SCORE, 5)
		],
		NEXT:MORNING_HUNGER_2
	},
	DUCK_BEFRIEND_FAIL:{
		TEXT:[
			"You try and befriend the duck, but it doesn't really care for you.", "It seems to be sitting on a nest."
		],
		NEXT:GETTING_LATE
	},
	NEST_SITTING_1:{
		TEXT:[
			""
		],
	},
	GETTING_LATE:{
		TEXT:[
			"Well, it's getting late. You should probably go to bed."
		],
		NEXT:UNEVENTFUL_NIGHT_3
	},
	UNEVENTFUL_DAY_1:{
		TEXT:[
			"Nothing eventful happens throughout the day."
		],
		NEXT:UNEVENTFUL_NIGHT_2
	},
	UNEVENTFUL_NIGHT_2:{
		TEXT:[
			"You spend the night on the rainforest floor and have an uneventful night. Time to start the day!"
		],
		ACTIONS:[
			(INCREASE_DAYS, 1),
			(INCREASE_SCORE, 1)
		],
		CHANCE:[(.7, MORNING_HUNGER_1), (.2, SWIMMING_URGE), (.1, WAKE_UP_SNAKE)]	
	},
	WAKE_UP_SNAKE:{
		TEXT:[
			"You wake up and see something bright and multicolored far away but you're not sure what it is."
		],
		OPTIONS:[
			{TEXT:"Fly away", NEXT:RETURN_TO_LAND_2},
			{TEXT:"It's obivously a mallard. Try and court it", NEXT:SNAKE_POISON_DEATH_2},
			{TEXT:"Go closer", NEXT:SNAKE_IDENTIFY}
		]
	},
	RETURN_TO_LAND_2:{
		TEXT:[
			"Phew! That was a close one!"
		],
		NEXT:GETTING_LATE
	},
	SNAKE_POISON_DEATH_2:{
		TEXT:[
			"You run towards it to try and court it, but then realize it's a venomous snake-- too late.", "GAME OVER"
		],
		ACTIONS:[
			(GAME_OVER, None)
		]
	},
	SNAKE_IDENTIFY:{
		TEXT:[
			"You go closer and eventually realize it's a snake and fly away."
		],
		NEXT:RETURN_TO_LAND_2
	},
	SNAKE_FLEE:{
		TEXT:[
			"You start quacking like mad and eventually see a snake flee from the tree trunk that you might have ", 
			"wanted to sleep in. You decide not to sleep in there."
		],
		NEXT:UNEVENTFUL_NIGHT_1
	},
	UNEVENTFUL_NIGHT_3:{
		TEXT:[
			"You have a mainly undisturbed night aside from the sounds of the rainforest."
		],
		ACTIONS:[
			(INCREASE_SCORE, 1),
			(INCREASE_DAYS, 1)
		],
		CHANCE:[(.5, MORNING_HUNGER_1), (.2, SWIMMING_URGE), (.3, MORNING_ENCOUNTER_1)]
	},
	MORNING_ENCOUNTER_1:{
		TEXT:[
			"You wake up and see some strange thing in the distance.", 
			"You can't quite tell that it is from here. It looks large, though."
		],
		OPTIONS:[
			{TEXT:"Fly away", CHANCE:[(.5, DUCK_HUNTER_DEATH), (.5, BAD_AIM)]},
			{TEXT:"Hide", NEXT:DUCK_HUNTER_SEE},
			{TEXT:"Go towards it", NEXT:DUCK_HUNTER_DEATH}
		]
	},
	DUCK_HUNTER_DEATH:{
		TEXT:[
			"It was a duck hunter! You alerted it to you position.", "GAME OVER"
		],
		ACTIONS:[
			(GAME_OVER, None)
		]
	},
	BAD_AIM:{
		TEXT:[
			"A bullet whizzes through the air. It was a duck hunter! He must not be a good shot.", 
			"You manage to safely get away from him."
		],
		NEXT:UNEVENTFUL_DAY_1
	},
	DUCK_HUNTER_SEE:{
		TEXT:[
			"You hide in some tall grass and you see that the large figure was in fact a DUCK HUNTER!", 
			"You manage to avoid him, however."
		],
		NEXT:UNEVENTFUL_DAY_1
	},
	NEST_SITTING_2:{
		TEXT:[
			"A few months later, after surviving for quite a bit, you feel a strange urge in your belly.",
			"Wait... wait... it's happening... *pop* You just laid an egg! Three, in fact!",
			"Now, since I don't want you to play for hundreds more days, you only have to lay on the eggs",
			"and keep them and yourself alive for a week."
		],
		ACTIONS:[
			(INCREASE_DAYS, 104),
			(INCREASE_SCORE, 104)
		],
		OPTIONS:[
			{TEXT:"Keep sitting", NEXT:KEEP_SITTING_1},
			{TEXT:"Leave", NEXT:HEARTLESS_MOTHER}
		]
	},
	KEEP_SITTING_1:{ 
		TEXT:[
			"You sit on the nest for an entire day and an entire night and are now very hungry."
		],
		OPTIONS:[
			{TEXT:"Keep sitting", NEXT:EXTREME_HUNGER},
			{TEXT:"Go get food", NEXT:EGGS_EATEN},
			{TEXT:"Try and find food within viewing distance of the nest", NEXT:STILL_SITTING_1}
		]
	},
	EXTREME_HUNGER:{ 
		TEXT:[
			"You are a very determined mother and I value that, but you did just starve to death," 
			"so I have to give you a game over, but I'll give you an extra 25 points.",
		],
		ACTIONS:[
			(INCREASE_SCORE, 25),
			(GAME_OVER, None)
		]
	},
	EGGS_EATEN:{
		TEXT:[
			"After you go get some food, you come back to an empty nest. Your eggs have been eaten!",
			"GAME OVER"
		],
		ACTIONS:[
			(GAME_OVER, None)
		]
	},
	STILL_SITTING_1:{ 
		TEXT:[
			"You manage to find some food within viewing distance of your nest, and eventually scare off an",
			"animal trying to eat your eggs."
		],
		NEXT:STILL_SITTING_2
	},
	STILL_SITTING_2:{
		TEXT:[
			"The rest of your egg-sitting goes pretty uneventfully... until now.",
			"IT'S HAPPENING!!!"
		],
		ACTIONS:[
			(INCREASE_BABIES_RESPECT, 80),
			(INCREASE_BABIES, 3)
		],
		NEXT:SO_CUTE
	},
	STILL_SITTING_3:{
		TEXT:[
			"The rest of your egg-sitting goes pretty uneventfully... until now.",
			"IT'S HAPPENING!!!"
		],
		ACTIONS:[
			(INCREASE_BABIES_RESPECT, 80),
			(INCREASE_BABIES, 4)
		],
		NEXT:SO_CUTE
	},
	SO_CUTE:{
		TEXT:[
			"Awww, they're so cute! What do you want to do with them first?"
		],
		OPTIONS:[
			{TEXT:"Feed them", NEXT:BABIES_FED},
			{TEXT:"Go swimming", NEXT:HUNGRY_BABIES},
			{TEXT:"Go flying", NEXT:WOW_JUST_WOW},
		]
	},
	HUNGRY_BABIES:{
		TEXT:[
			"After a while, your babies learn to swim and go swimming with you,",
			"but they are now very hungry and one of them got lost."
		],
		ACTIONS:[
			(INCREASE_BABIES, -1),
			(INCREASE_BABIES_RESPECT, -10)
		],
		NEXT:BABIES_FED
	},
	BABIES_FED:{
		TEXT:[
			"You feed the babies some food you found and they're no longer hungry."
		],
		ACTIONS:[
			(INCREASE_BABIES_RESPECT, 1)
		],
		NEXT:GETTING_LATE
	},
	WOW_JUST_WOW:{
		TEXT:[
			"You stupid duck! Newborn ducklings can't fly!",
			"GAME OVER"
		],
		ACTIONS:[
			(GAME_OVER, None)
		]
	},
	HEARTLESS_MOTHER:{
		TEXT:[
			"Wow. Leaving as soon as you laid the eggs. Now, that's just cruel. So, you know what?",
			"GAME OVER"
		],
		ACTIONS:[
			(GAME_OVER, None)
		]
	}
}

class DialogTree:
	def __init__(self, manager, data_map, event_key = START):
		self.manager = manager
		self.data_map = data_map
		self.event_key = event_key

	def make_selection(self, index):
		if self.manager.can_restart: 
			self.manager.restart()
			return
		event_map = self.get_current_event_map()
		if ACTIONS in event_map:
			actions = event_map[ACTIONS]
			for a in actions: self.execute_action(a)		
		options = self.get_current_options(event_map)
		if not options: 
			self.advance_to_next()
			return
		if NEXT in options[index]: self.event_key = options[index][NEXT]
		else:
			chance_data = options[index][CHANCE]
			roll = random.uniform(0, 1)
			print roll
			roll_test = 0
			for c in chance_data:
				roll_test += c[0]
				if roll < roll_test:
					self.event_key = c[1]
					return

	def advance_to_next(self):
		event_map = self.get_current_event_map()
		if CHANCE in event_map: 
			chance_data = event_map[CHANCE]
			roll = random.uniform(0, 1)
			print roll
			roll_test = 0
			for c in chance_data:
				roll_test += c[0]
				if roll < roll_test:
					self.event_key = c[1]
					return
		elif NEXT in event_map:
			next_data = event_map[NEXT]
			self.event_key = next_data

	def execute_action(self, action_data):
		action = ACTION_MAP[action_data[0]]
		action(self, action_data[1])

	def game_over(self, arg):
		self.manager.add_restart_button()

	def increment_days(self, days):
		self.manager.days += days

	def increment_score(self, score):
		self.manager.score += score

	def increment_babies(self, babies):
		self.manager.babies += babies

	def increment_babies_respect(self, respect):
		self.manager.babies_respect += respect
		if self.manager.babies_respect <= 0: self.event_key = LOSE_ALL_BABIES_RESPECT

	def get_current_text(self):
		return self.get_current_event_map()[TEXT]

	def get_current_options(self, event_map):
		if OPTIONS in event_map: return event_map[OPTIONS]
		return None

	def option_count(self):
		options = self.get_current_options(self.get_current_event_map())
		if not options: return 0
		else: return len(options)

	def get_current_event_map(self):
		event_map = self.data_map[self.event_key]
		if BABY_VERSION in event_map and self.manager.babies > 0: event_map = event_map[BABY_VERSION]
		return event_map

ACTION_MAP = {
	INCREASE_DAYS:DialogTree.increment_days,
	INCREASE_SCORE:DialogTree.increment_score,
	INCREASE_BABIES:DialogTree.increment_babies,
	INCREASE_BABIES_RESPECT:DialogTree.increment_babies_respect,
	GAME_OVER:DialogTree.game_over
}