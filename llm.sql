-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2024-05-22 15:58:15
-- 服务器版本： 10.4.28-MariaDB
-- PHP 版本： 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `llm`
--

-- --------------------------------------------------------

--
-- 表的结构 `assignq`
--

CREATE TABLE `assignq` (
  `id` int(11) NOT NULL,
  `qCode` varchar(100) DEFAULT NULL,
  `qText` varchar(300) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `assignq`
--

INSERT INTO `assignq` (`id`, `qCode`, `qText`, `course_id`, `status`) VALUES
(1, '6', 'Evaluate the integral:∫2_1^9▒〖4/5 𝑥^3−3/4 𝑥^2+2/5 𝑥〗  𝑑𝑥\r\n∫2_1^3▒〖𝑥^2+2𝑥−4〗 𝑑𝑥\r\n∫1▒〖1/2  cos⁡5𝑥 〗 𝑑𝑥^2\r\n', 4, 1),
(2, '7', 'Determine whether the following relations are reflexive, symmetric, antisymmetric, or transitive.', 1, 1),
(3, '1', 'how to write bar chart？', 3, 1),
(4, '2', 'how to write column chart?', 3, 1),
(5, '8', 'Implement the Queue structure use the standard C language.', 2, 1),
(6, '9', 'Determine whether the following sets of vectors are linearly independent: (1) [2,1, -1], [0, -4, 8], [1, -1, 3] (Note that these three sets of vectors are three-by-one)', 6, 1),
(7, '3', 'what is second derivative?', 4, 1),
(8, '4', 'how to do unit test?', 5, 1),
(9, '5', 'how to do software development?', 5, 1),
(10, '10', '{13, 14, 16, 17, 19, 20, 20, 21, 22, 23, 24, 25, 25, 30, 33, 33, 35, 35, 35, 35, 39, 42, 45, 50, 72}. \r\nfind the mean , mode and median of these values.', 7, 1),
(11, '11', 'Find the gradient of f at the point P(2,-1.1). Find the maximum rate if change of f at P and the direction in which it occurs. Calculate the directional derivative of f at the point P in the direction of the vector u=(0,0.8,-0.6)', 8, 1),
(12, '12', 'Please write a C language program that receives an array of length n, converts it into a linked list, and exchanges the first two nodes and the last two nodes of the linked list, and outputs the linked list after the exchange position.', 2, 1),
(13, '13', 'Modify a .py file provided to take two columns in the csv file for linear regression prediction', 9, 1),
(14, '14', 'Please write an Argumentative Essay, no topic limitation for you.', 10, 1),
(15, '1', 'Let R_1, R_2 be two arbitrary relations on an arbitrary set A.', 1, 1);

-- --------------------------------------------------------

--
-- 表的结构 `course`
--

CREATE TABLE `course` (
  `id` int(11) NOT NULL,
  `cName` varchar(50) DEFAULT NULL,
  `cNumber` int(11) DEFAULT NULL,
  `category` enum('COMP','MATH','WRIT') NOT NULL,
  `status` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `course`
--

INSERT INTO `course` (`id`, `cName`, `cNumber`, `category`, `status`) VALUES
(1, 'Discrete Mathematics', 165, 'MATH', 1),
(2, 'Data Structure and Algorithm', 166, 'COMP', 1),
(3, 'Infographics', 164, 'WRIT', 1),
(4, 'calculus', 478, 'MATH', 1),
(5, 'sdw', 714, 'COMP', 1),
(6, 'Linear Algebra', 167, 'MATH', 1),
(7, 'Data Mining and Knowledge Discover', 168, 'COMP', 1),
(8, 'Advance Calculus', 169, 'MATH', 1),
(9, 'Machine Learning', 170, 'COMP', 1),
(10, 'English', 171, 'WRIT', 1),
(11, 'Chinese', 172, 'WRIT', 1);

-- --------------------------------------------------------

--
-- 表的结构 `experiments`
--

CREATE TABLE `experiments` (
  `id` int(11) NOT NULL,
  `vCode` varchar(100) DEFAULT NULL,
  `vText` varchar(100) DEFAULT NULL,
  `LLM_name` varchar(100) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  `status` enum('IN_GENERAL_DATABASE','SUBMITTED','NOT_SUBMITTED') NOT NULL,
  `answer_img` varchar(100) DEFAULT NULL,
  `question_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `experiments`
--

INSERT INTO `experiments` (`id`, `vCode`, `vText`, `LLM_name`, `score`, `comment`, `status`, `answer_img`, `question_id`, `user_id`) VALUES
(1, '1', 'Let R_1, R_2 be two arbitrary relations on an arbitrary set A.', 'ChatGPT4.0', 4, 'Answers are correct with detailed process.', 'IN_GENERAL_DATABASE', '/images/Figure16.1.1.png\r\n', 15, 2),
(2, '3', 'wer', 'gpt4.0', 3, '3', 'IN_GENERAL_DATABASE', '/images/OIP.jpg', 3, 2),
(3, '5', 'how to write better column chart!', 'gpt3.5', 3, 'ok', 'IN_GENERAL_DATABASE', '/images/OIP.jpg', 4, 2),
(4, '2', 'how to avoid paraphrase?', 'AI 1.0', 1, 'hiha', 'IN_GENERAL_DATABASE', '/images/OIP.jpg', 4, 2),
(5, '2', 'Let R_1, R_2 be two arbitrary relations on an arbitrary set A.', 'Claude 2.0', 1, 'Most not correct but the process is acceptable to read.', 'IN_GENERAL_DATABASE', '/images/Figure16.2.1.png\r\n', 15, 2),
(6, '3', 'Let R_1, R_2 be two arbitrary relations on an arbitrary set A.', 'ERNIE Bot 3.5', 0, 'The processes are too simple to read cannot been seen it as correct answer.', 'IN_GENERAL_DATABASE', '/images/Figure16.3.1.png', 15, 2);

-- --------------------------------------------------------

--
-- 表的结构 `helptopic`
--

CREATE TABLE `helptopic` (
  `coursetype` varchar(30) DEFAULT NULL,
  `topicid` int(11) NOT NULL COMMENT 'ID',
  `topic` varchar(50) DEFAULT NULL,
  `subtopic` varchar(50) DEFAULT NULL,
  `topicq` varchar(200) DEFAULT NULL,
  `topica` varchar(400) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `helptopic`
--

INSERT INTO `helptopic` (`coursetype`, `topicid`, `topic`, `subtopic`, `topicq`, `topica`, `course_id`, `status`) VALUES
('MATH', 1, 'Discrete mathematics', 'arbitrary set ', 'Let R_1, R_2 be two arbitrary relations on an arbitrary set A.', 'In relational algebra, 𝑅1 and 𝑅2  are two relations defined on the same set 𝐴A. This means that the tuples (rows) in both 𝑅1R 1 and 𝑅2\r\nconsist of elements from 𝐴.', 1, 1),
('MATH', 2, 'Calculus', 'Sketch', 'Sketch the graph of the function :y=(𝑥+2)^2  〖(𝑥−1)〗^3', 'To sketch the graph, follow these steps:\r\nPlot the x-intercepts, if any, by setting 𝑦=0\r\ny=0 and solving for 𝑥.\r\nPlot the y-intercept by setting 𝑥=0and solving for 𝑦.', 4, 1),
('MATH', 3, 'Calculus', 'integrals', 'Find the definite integrals of below functions: ', ' it seems there was an omission in your message—you didn\'t provide the specific functions for which you\'d like to find the definite integrals. ', 4, 1),
('MATH', 4, 'Calculus', 'Expression', 'Find an expression for the function whose graph is the given in figure', 'It seems there might be a misunderstanding, as there is no figure provided in your message. To help you find an expression for a function based on its graph, I would need to see the graph or have a description of its key features, such as:', 4, 1),
('COMP', 5, 'Computer science', 'Python', 'Please write a Python program to sort a given list, the time complexity of the program should be O(nlogn)', 'def merge_sort(arr):\r\n    if len(arr) > 1:\r\n        mid = len(arr) // 2  # Finding the mid of the array\r\n        left_half = arr[:mid]  # Dividing the array elements into 2 halves\r\n        right_half = arr[mid:]\r\n\r\n        merge_sort(left_half)  # Sorting the first half\r\n        merge_sort(right_half)  # Sorting the second half\r\n\r\n        i = j = k = 0\r\n\r\n        # Copy data to temp arrays left_ha', 2, 1),
('WRIT', 6, 'Chinese', 'Reaction', 'Write a reaction to Lu Xun’s book Wa', '鲁迅是中国现代文学中最杰出的人物之一，以其犀利和批判的写作风格而闻名。他的《呐喊》是一部短篇小说集，是对20世纪初中国社会的批判。值得注意的是，《佤族》并不是鲁迅的一本专著;相反，这是他1922年出版的第一部短篇小说集的标题，其中包括著名的《疯子日记》等。', 11, 1),
('MATH', 7, 'Calculus', 'Evaluate question', 'Evaluate those functios:', 'It seems like you\'re asking to evaluate some functions, but you haven\'t specified which functions you\'re referring to. Could you please provide the functions you\'d like me to evaluate, along with any specific values or conditions for the evaluation? For example, you might want to evaluate a mathematical function like', 4, 1),
('MATH', 8, 'Calculus', 'Proof question', 'Proof equation can be changed to others forms.', 'In mathematics, equations can often be transformed into various forms to make them easier to solve or to provide different insights. Here are some common ways in which equations can be changed or manipulated:', 4, 1),
('MATH', 10, 'Discrete mathematics', 'Relations', 'Determine whether the following relations are reflexive, symmetric, antisymmetric, or transitive', 'To determine whether a relation has certain properties, we need to understand the definitions of reflexive, symmetric, antisymmetric, and transitive relations:', 1, 1);

-- --------------------------------------------------------

--
-- 表的结构 `llmanswer`
--

CREATE TABLE `llmanswer` (
  `id` int(11) NOT NULL,
  `_LLM_Name` varchar(50) DEFAULT NULL,
  `_LLMAnswerImg` varchar(200) DEFAULT NULL,
  `_answerID` varchar(50) DEFAULT NULL,
  `variation_id` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `llmanswer`
--

INSERT INTO `llmanswer` (`id`, `_LLM_Name`, `_LLMAnswerImg`, `_answerID`, `variation_id`, `status`) VALUES
(2, 'gpt3.5', '/images/OIP.jpg', NULL, 4, 1),
(3, 'gpt4.0', '/images/OIP.jpg', NULL, 5, 1),
(4, 'AI 1.0', '/images/OIP.jpg', NULL, 6, 1),
(5, 'gpt4.0', '/images/OIP.jpg', NULL, 7, 1),
(6, 'gpt3.5', '/images/OIP.jpg', NULL, 11, 1),
(7, 'AI 2.0', '/images/OIP.jpg', NULL, 12, 1),
(8, 'gpt4.0', '/images/OIP.jpg', NULL, 13, 1),
(9, 'AI 1.0', '/images/OIP.jpg', NULL, 14, 1),
(10, 'ChatGPT4.0', '/images/Figure1.1.png', NULL, 1, 1),
(11, 'Claude 2.0', '/images/Figure1.2.png', NULL, 1, 1),
(12, 'ERNIE Bot 3.5', '/images/Figure1.3.1.png\r\n/images/Figure1.3.2.png\r\n/images/Figure1.3.3.png', NULL, 1, 1),
(13, 'ChatGPT4.0', '/images/Figure2.1.1.png\r\n/images/Figure2.1.2.png', NULL, 2, 1),
(14, 'Claude 2.0', '/images/Figure2.2.1.png\r\n/images/Figure2.2.2.png', NULL, 2, 1),
(15, 'ERNIE Bot 3.5', '/images/Figure2.3.1.png\r\n/images/Figure2.3.2.png\r\n/images/Figure2.3.3.png', NULL, 2, 1),
(16, 'ChatGPT4.0', '/images/Figure3.1.1.png\r\n/images/Figure3.1.2.png', NULL, 3, 1),
(17, 'Claude 2.0', '/images/Figure3.2.1.png\r\n/images/Figure3.2.2.png', NULL, 3, 1),
(18, 'ERNIE Bot 3.5', '/images/Figure3.3.1.png\r\n/images/Figure3.3.2.png\r\n', NULL, 3, 1),
(19, 'ChatGPT3.5', '/images/Figure4.1.1.png\r\n/images/Figure4.1.2.png\r\n/images/Figure4.1.3.png\r\n/images/Figure4.1.4.png', NULL, 8, 1),
(20, 'Claude 2.0', '/images/Figure4.2.1.png', NULL, 8, 1),
(21, 'ERNIE Bot 3.5', '/images/Figure4.3.1.png', NULL, 8, 1),
(22, 'ChatGPT3.5', '/images/Figure5.1.1.png', NULL, 9, 1),
(23, 'ERNIE Bot 3.5', '/images/Figure5.2.1.png', NULL, 9, 1),
(24, 'ChatGPT3.5', '/images/Figure6.1.1.png', NULL, 10, 1),
(25, 'ERNIE Bot 3.5', '/images/Figure6.2.1.png', NULL, 10, 1),
(26, 'ChatGPT3.5', '/images/Figure7.1.1.png\r\n/images/Figure7.1.2.png\r\n/images/Figure7.1.3.png\r\n/images/Figure7.1.4.png', NULL, 15, 1),
(27, 'ERNIE Bot 3.5', '/images/Figure7.2.1.png\r\n/images/Figure7.2.2.png\r\n/images/Figure7.2.3.png', NULL, 15, 1),
(28, 'ChatGPT3.5', '/images/Figure8.1.1.png\r\n/images/Figure8.1.2.png', NULL, 16, 1),
(29, 'ERNIE Bot 3.5', '/images/Figure8.2.1.png\r\n/images/Figure8.2.2.png\r\n/images/Figure8.2.3.png\r\n/images/Figure8.2.4.png\r\n/images/Figure8.2.5.png\r\n/images/Figure8.2.6.png', NULL, 16, 1),
(30, 'ChatGPT3.5', '/images/Figure9.1.1.png', NULL, 17, 1),
(31, 'ERNIE Bot 3.5', '/images/Figure9.2.1.png', NULL, 17, 1);

-- --------------------------------------------------------

--
-- 表的结构 `llmscore`
--

CREATE TABLE `llmscore` (
  `id` int(11) NOT NULL,
  `score` int(11) DEFAULT NULL,
  `comment` varchar(300) DEFAULT NULL,
  `answer_id` int(11) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `llmscore`
--

INSERT INTO `llmscore` (`id`, `score`, `comment`, `answer_id`, `teacher_id`, `status`) VALUES
(3, 3, 'ok', 2, 2, 1),
(4, 5, 'ok', 3, 2, 1),
(5, 1, 'ok', 4, 2, 1),
(6, 5, 'okok', 5, 2, 1),
(7, 3, 'okok', 3, 2, 1),
(8, 3, 'ok', 6, 2, 1),
(9, 4, 'ok', 2, 2, 1),
(10, 4, 'okok', 7, 2, 1),
(11, 3, '3', 8, 2, 1),
(12, 1, 'hiha', 9, 2, 1),
(13, 5, 'Fast respond, all answers are correct, with detailed explaination.', 10, 2, 1),
(14, 2, 'Fast respond, only 1 correct answer.', 11, 2, 1),
(15, 0, 'Slow respond, no correct answer.', 12, 2, 1),
(16, 3, 'Some answers are wrong, but for correct ones there are good explainations.', 13, 2, 1),
(17, 2, 'Over half of answers are wrong, however the process is detailed and easy to understand.', 14, 2, 1),
(18, 2, 'Half of answers are wrong, process is good.', 15, 2, 1),
(19, 3, 'The answer given is very normal, but the task is done well, and can be completed more accurately after feeding more details.', 16, 2, 1),
(20, 2, 'The program answered with an error, missing a library reference. The task is not accomplished, and the comments given are meaningless.', 17, 2, 1),
(21, 2, 'The requirements were fulfilled but no program was given that could be run directly.Some unnecessary and pointless comments were given.', 18, 2, 1),
(22, 3, 'The GPT module response quickly, doing great in progress and concept, but perform badly in calculation. And wrong answer.', 19, 2, 1),
(23, 2, 'Claude well organized in language, but it’s behavior in calculation is terrible.', 20, 2, 1),
(24, 1, 'It was very slow and didn’t show the calculation step and print the wrong answer', 21, 2, 1),
(25, 3, 'Got the wrong value of Mean', 22, 2, 1),
(26, 0, 'Made a mistake in understanding condition of the problem,that led to a total wrong result', 23, 2, 1),
(27, 2, 'Well understood the problem and had a correct interpretation. ', 24, 2, 1),
(28, 1, 'Could not interpret the problem correctly.', 25, 2, 1),
(29, 3, 'Misunderstood the meaning of the question, create two meaningless pointer： ” prevFirst” and “prevSecond”.\r\nAnd the requirement is to exchange the first node with the second node, and exchange the second to last node with the last node, but it did the wrong exchangethe data into the formula', 26, 2, 1),
(30, 4, 'Lack of memory release may lead to memory leakage. Only swapping node values, without actually swapping nodes.', 27, 2, 1),
(31, 5, 'Give the right figure out put, and the graph has more detail.', 28, 2, 1),
(32, 4, 'There is an error in the code.', 29, 2, 1),
(33, 4, 'Took 8 seconds to finish.', 30, 2, 1),
(34, 3, 'Almost no logical relationship can be found in this essay.', 31, 2, 1);

-- --------------------------------------------------------

--
-- 表的结构 `question_variation`
--

CREATE TABLE `question_variation` (
  `id` int(11) NOT NULL,
  `vCode` varchar(100) DEFAULT NULL,
  `vText` varchar(250) DEFAULT NULL,
  `question_id` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `question_variation`
--

INSERT INTO `question_variation` (`id`, `vCode`, `vText`, `question_id`, `status`) VALUES
(1, '1', 'Evaluate the integral:∫2_1^9▒〖4/5 𝑥^3−3/4 𝑥^2+2/5 𝑥〗  𝑑𝑥\r\n∫2_1^3▒〖𝑥^2+2𝑥−4〗 𝑑𝑥\r\n∫1▒〖1/2  cos⁡5𝑥 〗 𝑑𝑥^2\r\n', 1, 1),
(2, '1', 'Determine whether the following relations are reflexive, symmetric, antisymmetric, or transitive.', 2, 1),
(3, '1', 'Implement the Queue structure use the standard C language.', 5, 1),
(4, '1', 'how to write bar chart？', 3, 1),
(5, '2', 'how to write column chart?', 4, 1),
(6, '3', 'what is second derivative?', 7, 1),
(7, '4', 'how to do unit test?', 8, 1),
(8, '1', 'Determine whether the following sets of vectors are linearly independent: (1) [2,1, -1], [0, -4, 8], [1, -1, 3] (Note that these three sets of vectors are three-by-one)', 6, 1),
(9, '1', '{13, 14, 16, 17, 19, 20, 20, 21, 22, 23, 24, 25, 25, 30, 33, 33, 35, 35, 35, 35, 39, 42, 45, 50, 72}. \r\nfind the mean , mode and median of these values.', 10, 1),
(10, '1', 'Find the gradient of f at the point P(2,-1.1). Find the maximum rate if change of f at P and the direction in which it occurs. Calculate the directional derivative of f at the point P in the direction of the vector u=(0,0.8,-0.6)', 11, 1),
(11, '5', 'how to write better column chart!', 4, 1),
(12, '3', 'how to do software development?', 9, 1),
(13, '3', 'wer', 3, 1),
(14, '2', 'how to avoid paraphrase?', 4, 1),
(15, '1', 'Please write a C language program that receives an array of length n, converts it into a linked list, and exchanges the first two nodes and the last two nodes of the linked list, and outputs the linked list after the exchange position.', 12, 1),
(16, '1', 'Modify a .py file provided to take two columns in the csv file for linear regression prediction', 13, 1),
(17, '1', 'Please write an Argumentative Essay, no topic limitation for you.', 14, 1);

-- --------------------------------------------------------

--
-- 表的结构 `request`
--

CREATE TABLE `request` (
  `rid` int(11) NOT NULL,
  `request_type` enum('ADD_COURSE','ADD_QUESTION','UPDATE_SCORE','EXPERIMENT','ADD_TOPIC') NOT NULL,
  `col1` varchar(300) DEFAULT NULL,
  `col2` varchar(500) DEFAULT NULL,
  `col3` varchar(300) DEFAULT NULL,
  `col4` varchar(300) DEFAULT NULL,
  `col5` varchar(300) DEFAULT NULL,
  `col6` varchar(300) DEFAULT NULL,
  `col7` varchar(300) DEFAULT NULL,
  `col8` varchar(300) DEFAULT NULL,
  `status` enum('PASSED','REJECTED','PENDING') NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `request`
--

INSERT INTO `request` (`rid`, `request_type`, `col1`, `col2`, `col3`, `col4`, `col5`, `col6`, `col7`, `col8`, `status`, `user_id`) VALUES
(1, 'ADD_COURSE', 'Discrete Mathematics', '165', 'MATH', NULL, NULL, NULL, NULL, NULL, 'PASSED', 2),
(2, 'ADD_COURSE', 'Data Structure and Algorithm', '166', 'COMP', NULL, NULL, NULL, NULL, NULL, 'PASSED', 2),
(3, 'ADD_COURSE', 'Data Mining and Knowledge Discover\r\n', '168', 'COMP', NULL, NULL, NULL, NULL, NULL, 'PASSED', 2),
(4, 'ADD_COURSE', 'Advance Calculus', '169', 'MATH', NULL, NULL, NULL, NULL, NULL, 'PASSED', 2),
(5, 'ADD_COURSE', 'Machine Learning', '170', 'COMP', NULL, NULL, NULL, NULL, NULL, 'PASSED', 2),
(6, 'ADD_COURSE', 'English', '171', 'WRIT', NULL, NULL, NULL, NULL, NULL, 'PASSED', 2),
(7, 'ADD_COURSE', 'Chinese', '172', 'WRIT', NULL, NULL, NULL, NULL, NULL, 'PASSED', 2),
(8, 'ADD_COURSE', 'Infographics', '164', 'Writ', NULL, NULL, NULL, NULL, NULL, 'PASSED', 2),
(9, 'ADD_COURSE', 'calculus', '478', 'Math', NULL, NULL, NULL, NULL, NULL, 'PASSED', 2),
(10, 'ADD_COURSE', 'Linear Algebra', '789', 'Math', NULL, NULL, NULL, NULL, NULL, 'REJECTED', 2),
(11, 'ADD_COURSE', 'sdw', '714', 'Comp', NULL, NULL, NULL, NULL, NULL, 'PASSED', 2),
(12, 'ADD_QUESTION', '1', 'how to write bar chart？', '3', 'gpt3.5', '3', 'ok', '/images/Figure19.1.1.png', NULL, 'PASSED', 2),
(13, 'ADD_QUESTION', '2', 'how to write column chart?', '3', 'gpt4.0', '5', 'ok', '/images/Figure20.1.1.png', NULL, 'PASSED', 2),
(14, 'ADD_QUESTION', '2', 'what is second derivative?', '4', 'AI 1.0', '4', 'ok', '/images/Figure21.1.1.png', NULL, 'REJECTED', 2),
(15, 'ADD_QUESTION', '3', 'what is second derivative?', '4', 'AI 1.0', '1', 'ok', '/images/Figure21.1.1.png', NULL, 'PASSED', 2),
(16, 'ADD_QUESTION', '4', 'how to do unit test?', '5', 'gpt4.0', '5', 'okok', '/images/Figure22.1.1.png', NULL, 'PASSED', 2),
(17, 'UPDATE_SCORE', '3', '3', 'okok', NULL, NULL, NULL, NULL, NULL, 'PASSED', 2),
(18, 'EXPERIMENT', '3', '3', 'wer', 'gpt4.0', '3', '3', '/images/Figure20.1.1.png', '2', 'REJECTED', 2),
(19, 'EXPERIMENT', '3', '3', 'wer', 'gpt4.0', '3', '3', '/images/Figure20.1.1.png', '2', 'REJECTED', 2),
(20, 'EXPERIMENT', '4', '5', 'how to write better column chart!', 'gpt3.5', '3', 'ok', '/images/Figure23.1.1.png', '3', 'PASSED', 2),
(21, 'UPDATE_SCORE', '2', '4', 'ok', NULL, NULL, NULL, NULL, NULL, 'PASSED', 2),
(22, 'ADD_QUESTION', '3', 'how to do software development?', '5', 'KIMI', '4', 'goooooooooooooooooooooooood!!!!!!!!', '/images/Figure18.1.1.png', NULL, 'PASSED', 2),
(23, 'EXPERIMENT', '3', '3', 'wer', 'gpt4.0', '3', '3', '/images/Figure20.1.1.png', '2', 'PASSED', 2),
(24, 'EXPERIMENT', '4', '2', 'how to avoid paraphrase?', 'AI 1.0', '1', 'hiha', '/images/Figure23.1.1.png', '4', 'PASSED', 2),
(25, 'ADD_QUESTION', 'Calculus', 'Evaluate the integral:∫2_1^9▒〖4/5 𝑥^3−3/4 𝑥^2+2/5 𝑥〗  𝑑𝑥\r\n∫2_1^3▒〖𝑥^2+2𝑥−4〗 𝑑𝑥\r\n∫1▒〖1/2  cos⁡5𝑥 〗 𝑑𝑥^2\r\n', 'Math', 'CHATGPT4.0', '1', 'okok', '/images/Figure1.1.png', NULL, 'PASSED', 2),
(26, 'ADD_QUESTION', 'Discrete Mathematics', 'Determine whether the following relations are reflexive, symmetric, antisymmetric, or transitive.', 'Math', 'ChatGPT3.5', '1', 'okok', '/images/Figure2.1.1.png', NULL, 'PASSED', 2),
(27, 'ADD_QUESTION', 'calculus', 'Evaluate the integral:∫2_1^9▒〖4/5 𝑥^3−3/4 𝑥^2+2/5 𝑥〗  𝑑𝑥\r\n∫2_1^3▒〖𝑥^2+2𝑥−4〗 𝑑𝑥\r\n∫1▒〖1/2  cos⁡5𝑥 〗 𝑑𝑥^2\r\n', 'Math', 'Claude 2.0', '2', 'okok', '/images/Figure1.2.png', NULL, 'PASSED', 2),
(28, 'ADD_QUESTION', 'calculus', 'Evaluate the integral:∫2_1^9▒〖4/5 𝑥^3−3/4 𝑥^2+2/5 𝑥〗  𝑑𝑥\r\n∫2_1^3▒〖𝑥^2+2𝑥−4〗 𝑑𝑥\r\n∫1▒〖1/2  cos⁡5𝑥 〗 𝑑𝑥^2\r\n', 'Math', 'ERNIE Bot 3.5', '3', 'okok', '/images/Figure1.3.1.png', NULL, 'PASSED', 2),
(30, 'ADD_TOPIC', 'Computer science', 'Python', 'COMP', 'Please write a Python program to sort a given list, the time complexity of the program should be O(nlogn)', '/images/Figure17.2.1.png', '2', '', NULL, 'PASSED', 2),
(31, 'ADD_TOPIC', 'Chinese', 'Reaction', 'WRIT', 'Write a reaction to Lu Xun’s book Wa', '/images/Figure17.1.1.png', '11', NULL, NULL, 'PASSED', 2),
(32, 'UPDATE_SCORE', '10', '5', 'add wrong score', NULL, NULL, NULL, NULL, NULL, 'PASSED', 2),
(33, 'UPDATE_SCORE', '11', '2', 'add wrong score', NULL, NULL, NULL, NULL, NULL, 'PASSED', 2),
(34, 'ADD_QUESTION', 'Discrete mathematics', 'Let R_1, R_2 be two arbitrary relations on an arbitrary set A.', 'Math', 'ChatGPT4.0', '4', 'Answers are correct with detailed process.', '/images/Figure16.1.1.png', NULL, 'PASSED', 2),
(35, 'ADD_QUESTION', 'Calculus', 'Sketch the graph of the function :y=(𝑥+2)^2  〖(𝑥−1)〗^3', 'Math', 'ChatGPT3.5', '2', 'Most not correct but the process is acceptable to read.', '/images/Figure10.1.1.png', NULL, 'PASSED', 2),
(36, 'ADD_TOPIC', 'Calculus', 'integrals', 'Math', 'Find the definite integrals of below functions: ', '/images/Figure10.1.1.png', '4', NULL, NULL, 'PASSED', 2);

-- --------------------------------------------------------

--
-- 表的结构 `Topic_experiment`
--

CREATE TABLE `Topic_experiment` (
  `eid` int(11) NOT NULL,
  `vTxt` varchar(100) DEFAULT NULL,
  `LLMused` varchar(100) DEFAULT NULL,
  `answer` varchar(100) DEFAULT NULL,
  `score` float DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `Topic_experiment`
--

INSERT INTO `Topic_experiment` (`eid`, `vTxt`, `LLMused`, `answer`, `score`, `status`) VALUES
(1, 'Find the definite integrals of below functions: ', 'ai2.0', '1', 1, 1);

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `utype` enum('Teacher','Student','Admin') NOT NULL,
  `status` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`id`, `email`, `password`, `utype`, `status`) VALUES
(1, '123@mail.uic.edu.cn', '$2b$12$skimXux.lVeLSi4FNLLDd.8gpiXu/4pGI6zKNBq5T.E93ppcQ0KRi', 'Student', 1),
(2, '132@uic.edu.cn', '$2b$12$41OXxgtKiVe2rWb4O2nXAuRylRsdGh9DFk7cdvJ2JcRD6yGXQYtl6', 'Admin', 1);

--
-- 转储表的索引
--

--
-- 表的索引 `assignq`
--
ALTER TABLE `assignq`
  ADD PRIMARY KEY (`id`),
  ADD KEY `course_id` (`course_id`);

--
-- 表的索引 `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `experiments`
--
ALTER TABLE `experiments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `question_id` (`question_id`),
  ADD KEY `user_id` (`user_id`);

--
-- 表的索引 `helptopic`
--
ALTER TABLE `helptopic`
  ADD PRIMARY KEY (`topicid`),
  ADD KEY `course_id` (`course_id`);

--
-- 表的索引 `llmanswer`
--
ALTER TABLE `llmanswer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `_answerID` (`_answerID`),
  ADD KEY `variation_id` (`variation_id`);

--
-- 表的索引 `llmscore`
--
ALTER TABLE `llmscore`
  ADD PRIMARY KEY (`id`),
  ADD KEY `answer_id` (`answer_id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- 表的索引 `question_variation`
--
ALTER TABLE `question_variation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `question_id` (`question_id`);

--
-- 表的索引 `request`
--
ALTER TABLE `request`
  ADD PRIMARY KEY (`rid`),
  ADD KEY `user_id` (`user_id`);

--
-- 表的索引 `Topic_experiment`
--
ALTER TABLE `Topic_experiment`
  ADD PRIMARY KEY (`eid`);

--
-- 表的索引 `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `assignq`
--
ALTER TABLE `assignq`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- 使用表AUTO_INCREMENT `course`
--
ALTER TABLE `course`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- 使用表AUTO_INCREMENT `experiments`
--
ALTER TABLE `experiments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- 使用表AUTO_INCREMENT `helptopic`
--
ALTER TABLE `helptopic`
  MODIFY `topicid` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID', AUTO_INCREMENT=11;

--
-- 使用表AUTO_INCREMENT `llmanswer`
--
ALTER TABLE `llmanswer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- 使用表AUTO_INCREMENT `llmscore`
--
ALTER TABLE `llmscore`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- 使用表AUTO_INCREMENT `question_variation`
--
ALTER TABLE `question_variation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- 使用表AUTO_INCREMENT `request`
--
ALTER TABLE `request`
  MODIFY `rid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- 使用表AUTO_INCREMENT `Topic_experiment`
--
ALTER TABLE `Topic_experiment`
  MODIFY `eid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用表AUTO_INCREMENT `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 限制导出的表
--

--
-- 限制表 `assignq`
--
ALTER TABLE `assignq`
  ADD CONSTRAINT `assignq_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`);

--
-- 限制表 `experiments`
--
ALTER TABLE `experiments`
  ADD CONSTRAINT `experiments_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `assignq` (`id`),
  ADD CONSTRAINT `experiments_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- 限制表 `helptopic`
--
ALTER TABLE `helptopic`
  ADD CONSTRAINT `helptopic_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`);

--
-- 限制表 `llmanswer`
--
ALTER TABLE `llmanswer`
  ADD CONSTRAINT `llmanswer_ibfk_1` FOREIGN KEY (`variation_id`) REFERENCES `question_variation` (`id`);

--
-- 限制表 `llmscore`
--
ALTER TABLE `llmscore`
  ADD CONSTRAINT `llmscore_ibfk_1` FOREIGN KEY (`answer_id`) REFERENCES `llmanswer` (`id`),
  ADD CONSTRAINT `llmscore_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `user` (`id`);

--
-- 限制表 `question_variation`
--
ALTER TABLE `question_variation`
  ADD CONSTRAINT `question_variation_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `assignq` (`id`);

--
-- 限制表 `request`
--
ALTER TABLE `request`
  ADD CONSTRAINT `request_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
