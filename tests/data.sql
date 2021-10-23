-- ###########################################################
-- User
-- ###########################################################

CREATE TABLE `User` (
  `user_id` Int NOT NULL AUTO_INCREMENT,
  `email` Varchar(40),
  `phone_number` Varchar(10),
  `sim_type` Varchar(15),
  `password` Varchar(250),
  `first_name` Varchar(30),
  `last_name` Varchar(30),
  `reg_date` Varchar(30),
  `current_balance` float(5),
  `anytime_data` int,
  `night_time_data` int,
  `4g_data` int,
  PRIMARY KEY (`user_id`)
);

CREATE TABLE `Complaint` (
  `complaint_id` Int NOT NULL AUTO_INCREMENT,
  `user_id` Int,
  `isp` Varchar(20),
`subject` Varchar(300),
  `message` Varchar(1500),
  PRIMARY KEY (`complaint_id`),
  FOREIGN KEY (`user_id`) REFERENCES `User`(`user_id`)
);

CREATE TABLE `Chat` (
  `chat_id` Int NOT NULL AUTO_INCREMENT,
  `user_id` Int,
  PRIMARY KEY (`chat_id`),
  FOREIGN KEY (`user_id`) REFERENCES `User`(`user_id`)
);

CREATE TABLE `Message` (
  `message_id` Int NOT NULL AUTO_INCREMENT,
  `chat_id` Int,
  `type` Varchar(20),
  `message` Varchar(250),
  `sent_date` Varchar(30),
  PRIMARY KEY (`message_id`),
  FOREIGN KEY (`chat_id`) REFERENCES `Chat`(`chat_id`)
);


CREATE TABLE `Feedback` (
  `feedback_id` Int NOT NULL AUTO_INCREMENT,
  `user_id` Int,
   `chatbot_type` Varchar(60),
  `rating` int,
  `feedback` Varchar(150),
  PRIMARY KEY (`feedback_id`),
  FOREIGN KEY (`user_id`) REFERENCES `User`(`user_id`)
);

-- ###########################################################
-- Telecom
-- ###########################################################

CREATE TABLE `DataPackage` (
  `data_package_id` Int NOT NULL AUTO_INCREMENT,
  `connection` Varchar(40),
  `package_type` Varchar(120),
  `name` Varchar(80),
  `fee` Varchar(15),
  `anytime_data`Varchar(50),
  `night_time_data` Varchar(50),
  `4g_data` int,
  `details` Varchar(300),
  `validity_period` Varchar(50),
  PRIMARY KEY (`data_package_id`)
);

CREATE TABLE `VoicePackage` (
  `voice_package_id` Int NOT NULL AUTO_INCREMENT,
  `name` Varchar(40),
  `call_cost` Varchar(150),
  `available_free_voice` Varchar(150),
  `available_free_data` Varchar(150),
  `sms_cost` Varchar(150),
  `validity_period` Varchar(30),
  PRIMARY KEY (`voice_package_id`)
);






CREATE TABLE `ActivatedPackage` (
  `activation_id` Int NOT NULL AUTO_INCREMENT,
  `user_id` Int,
  `package_id` Int,
  `activated_date` Varchar(50),
  `validity_period` Varchar(50),
  PRIMARY KEY (`activation_id`),
  FOREIGN KEY (`user_id`) REFERENCES `User`(`user_id`),
  FOREIGN KEY (`package_id`) REFERENCES `DataPackage`(`data_package_id`)
);

-- ###########################################################
-- Healthcare
-- ###########################################################
CREATE TABLE `Doctor` (
  `doctorID` Int,
  `name` Varchar(20),
  `specialty` Varchar(50),
  `contact` Varchar(20),
  PRIMARY KEY (`doctorID`)
);

CREATE TABLE `Channel` (
  `channelID` Int NOT NULL AUTO_INCREMENT,
  `doctor` int,
  `userID` int,
  `time` Varchar(10),
  `date` Varchar(10),
  `hospital` Varchar(30),
  PRIMARY KEY (`channelID`),
  FOREIGN KEY (`userID`) REFERENCES `User`(`user_id`),
  FOREIGN KEY (`doctor`) REFERENCES `Doctor`(`doctorID`)
);

CREATE TABLE `Clinic` (
  `clinicID` Int NOT NULL AUTO_INCREMENT,
  `clinicType` Varchar(40),
  `doctor` Varchar(40),
  `date` Varchar(10),
  `time` Varchar(10),
	`place` Varchar(20),
  `unit` Varchar(20),
  PRIMARY KEY (`clinicID`)
);



-- ###########################################################
-- Public transportation
-- ###########################################################

CREATE TABLE `Route` (
  `routeID` Int NOT NULL AUTO_INCREMENT,
  `routeName` Varchar(50),
  `routeNo` Varchar(10),
  PRIMARY KEY (`routeID`)
);


CREATE TABLE `TransportationMethod` (
  `methodID` Int NOT NULL AUTO_INCREMENT,
  `routeID` Int,
  `type` Varchar(10),
  PRIMARY KEY (`methodID`),
  FOREIGN KEY (`routeID`) REFERENCES `Route`(`routeID`)
);

CREATE TABLE `Stop Station` (
  `stationID` Int NOT NULL AUTO_INCREMENT,
  `routeID` Int,
  `name` Varchar(20),
  `fee` Int,
  PRIMARY KEY (`stationID`),
  FOREIGN KEY (`routeID`) REFERENCES `TransportationMethod`(`methodID`)
);

CREATE TABLE `Departure Station` (
  `departureID` Int NOT NULL AUTO_INCREMENT,
  `routeID` Int,
  `name` Varchar(20),
  PRIMARY KEY (`departureID`),
  FOREIGN KEY (`routeID`) REFERENCES `TransportationMethod`(`methodID`)
);

CREATE TABLE `Destination Station` (
  `destinationID` Int NOT NULL AUTO_INCREMENT,
  `routeID` Int,
  `name` Varchar(20),
  `fee` Int,
  PRIMARY KEY (`destinationID`),
  FOREIGN KEY (`routeID`) REFERENCES `TransportationMethod`(`methodID`)
);



-- ###########################################################
-- Insert statements
-- ###########################################################

-- @@@@@@@@@@@@@@@@@@@@@@@@
-- Insert Statement - DataPackage
-- @@@@@@@@@@@@@@@@@@@@@@@@

-- Data Package Table
-- Mobitel - Mini internet plans
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Mini internet plans', 'Internet Chooty', '5' , '43', '0', '0', 'Excess Usage per MB(Only within validity period) Rs. 0.30', '1');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Mini internet plans', '3 Day Internet', '29' , '163', '163', '163', 'Excess Usage per MB(Only within validity period) Rs. 0.30', '3');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Mini internet plans', '7 Day Internet', '49' , '326', '326', '244', 'Excess Usage per MB(Only within validity period) Rs. 0.30', '7');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Mini internet plans', '21 Day Internet', '99' , '652', '652', '489', 'Excess Usage per MB(Only within validity period) Rs. 0.30', '21');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Mini internet plans', 'D199', '199' , '1413', '1413', '1087', 'Excess Usage per MB(Only within validity period) Rs. 0.30', '30');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Mini internet plans', 'D299', '299' , '2170', '2170', '1629', 'Excess Usage per MB(Only within validity period) Rs. 0.30', '30');

-- Mobitel - Anytime plans
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Anytime Plans', 'A49', '49' , '375', '0', '375', 'Excess Usage per MB Rs. 0.30', '7');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Anytime Plans', 'A99', '99' , '768', '0', '768', 'Excess Usage per MB Rs. 0.30', '21');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Anytime Plans', 'A199', '199' , '1690', '0', '1690', 'Excess Usage per MB Rs. 0.30', '30');

-- Mobitel - Best Value Pre-paid Internet Plans
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Best Value Pre-paid Internet Plans', 'D399', '399' , '2710', '2710', '2170', 'Excess Usage per MB(Only within validity period) Rs. 0.30', '30');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Best Value Pre-paid Internet Plans', 'D499', '499' , '4340', '3250', '3250', 'Excess Usage per MB(Only within validity period) Rs. 0.30', '30');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Best Value Pre-paid Internet Plans', 'D699', '699' , '6500', '5430', '4880', 'Excess Usage per MB(Only within validity period) Rs. 0.30', '30');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Best Value Pre-paid Internet Plans', 'D999', '999' , '8620', '8620', '6510', 'Excess Usage per MB(Only within validity period) Rs. 0.30', '30');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Best Value Pre-paid Internet Plans', 'D1999', '1999' , '21730', '21730', '16200', 'Excess Usage per MB(Only within validity period) Rs. 0.30', '365');

-- Mobitel - Prepaid Daily Plans
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Prepaid Daily Plans', 'Rs.5 Daily Plan', '5' , '40', '25', '0', '', '1');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Prepaid Daily Plans', 'Rs. 7 Daily Plans', '7' , '60', '60', '0', '', '1');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Prepaid Daily Plans', 'Rs. 9 Daily Plan', '9' , '80', '80', '0', '', '1');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Prepaid Daily Plans', 'Rs. 15 Daily Plan', '15' , '140', '140', '0', '', '1');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Mobitel', 'Prepaid Daily Plans', 'Rs. 25 Daily Plan', '25' , '250', '250', '0', '', '1');


-- Dialog - Any time data add ons
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Anytime Data Add-ons', '1GB - 1 Day', '60' , '1000', '0', '0', 'USSD: Dial #678# > Mobile Data > DATA ADD-ON Pack', '1');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Anytime Data Add-ons', '1GB - 7 Days', '80' , '1000', '0', '0', 'USSD: Dial #678# > Mobile Data > DATA ADD-ON Pack', '7');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Anytime Data Add-ons', '1GB - 30 Days', '100' , '1000', '0', '0', 'USSD: Dial #678# > Mobile Data > DATA ADD-ON Pack', '30');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Anytime Data Add-ons', '2GB - 1 Day', '100' , '2000', '0', '0', 'USSD: Dial #678# > Mobile Data > DATA ADD-ON Pack', '1');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Anytime Data Add-ons', '2GB - 7 Days', '140' , '2000', '0', '0', 'USSD: Dial #678# > Mobile Data > DATA ADD-ON Pack', '7');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Anytime Data Add-ons', '5GB - 1 Day', '225' , '5000', '0', '0', 'USSD: Dial #678# > Mobile Data > DATA ADD-ON Pack', '1');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Anytime Data Add-ons', '5GB - 7 Days', '320' , '5000', '0', '0', 'USSD: Dial #678# > Mobile Data > DATA ADD-ON Pack', '7');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Anytime Data Add-ons', '10GB - 1 Day', '350' , '10000', '0', '0', 'USSD: Dial #678# > Mobile Data > DATA ADD-ON Pack', '1');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Anytime Data Add-ons', '10GB - 7 Days', '525' , '10000', '0', '0', 'USSD: Dial #678# > Mobile Data > DATA ADD-ON Pack', '7');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Anytime Data Add-ons', '15GB - One Day', '450' , '15000', '0', '0', 'USSD: Dial #678# > Mobile Data > DATA ADD-ON Pack', '1');

INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Anytime Data Add-ons', '15GB - One Day', '700' , '15000', '0', '0', 'USSD: Dial #678# > Mobile Data > DATA ADD-ON Pack', '7');

-- Dialog - Internet Cards
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Internet Cards', 'Rs. 29', '29' , '165', '165', '82.5', 'USSD > Dial #678# and go to Mobile Data Plans and select Dialog Internet Cards', '3');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Internet Cards', 'Rs. 49', '49' , '330', '330', '165', 'USSD > Dial #678# and go to Mobile Data Plans and select Dialog Internet Cards', '7');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Internet Cards', 'Rs. 99', '99' , '660', '660', '330', 'USSD > Dial #678# and go to Mobile Data Plans and select Dialog Internet Cards', '21');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Internet Cards', 'Rs. 199', '199' , '1430', '1430', '710', 'USSD > Dial #678# and go to Mobile Data Plans and select Dialog Internet Cards', '30');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Internet Cards', 'Rs. 349', '349' , '2640', '2640', '1320', 'USSD > Dial #678# and go to Mobile Data Plans and select Dialog Internet Cards', '30');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Internet Cards', 'Rs. 499', '499' , '3960', '3960', '1980', 'USSD > Dial #678# and go to Mobile Data Plans and select Dialog Internet Cards', '30');

-- Dialog - Daily rental packages
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Internet Cards', 'Rs. 5', '5' , '40', '40', '20', 'USSD > Dial #678# and go to Mobile Data Plans and select Daily Blaster packages', '1');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Internet Cards', 'Rs. 10', '10' , '90', '90', '45', 'USSD > Dial #678# and go to Mobile Data Plans and select Daily Blaster packages', '1');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Dialog', 'Internet Cards', 'Rs. 20', '20' , '200', '200', '100', 'USSD > Dial #678# and go to Mobile Data Plans and select Daily Blaster packages', '1');


-- Hutch - Any Time Plans
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Hutch', 'Anytime Plans', 'Rs. 47', '47' , '600', '0', '0', 'USSD Activation - *131#', '5');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Hutch', 'Anytime Plans', 'Rs. 97', '97' , '1300', '0', '0', 'USSD Activation - *131#', '10');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Hutch', 'Anytime Plans', 'Rs. 197', '197' , '3000', '0', '0', 'USSD Activation - *131#', '21');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Hutch', 'Anytime Plans', 'Rs. 297', '297' , '4700', '0', '0', 'USSD Activation - *131#', '30');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Hutch', 'Anytime Plans', 'Rs. 497', '497' , '8200', '0', '0', 'USSD Activation - *131#', '30');

-- Hutch - Long Validity Plans
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Hutch', 'Long Validity Plans', '15 Days', '59' , '750', '0', '0', 'USSD Activation - *131#', '15');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Hutch', 'Long Validity Plans', '30 Days', '119' , '1500', '0', '0', 'USSD Activation - *131#', '30');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Hutch', 'Long Validity Plans', '45 Days', '239' , '3450', '0', '0', 'USSD Activation - *131#', '45');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Hutch', 'Long Validity Plans', '60 Days - 5.5GB', '369' , '5500', '0', '0', 'USSD Activation - *131#', '60');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Hutch', 'Long Validity Plans', '60 Days - 10GB', '619' , '10000', '0', '0', 'USSD Activation - *131#', '60');

-- Airtel - Data Downloader
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Airtel', 'Data Downloader', 'Rs.59', '59' , '330', '475', '206', 'To activate pack use Rs. 59 card', '4');
-- Airtel - Anytime Ranges
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Airtel', 'Anytime Range', 'Rs.118', '118' , '1000', '0', '332', 'To activate pack use Rs. 118 card', '10');
INSERT INTO `DataPackage`(`connection`,`package_type`,`name`,`fee`,`anytime_data`,`night_time_data`,`4g_data`, `details`, `validity_period`) VALUES('Airtel', 'Anytime Range', 'Rs.179', '179' , '1500', '0', '623', 'To activate pack use Rs. 118 card', '14');
