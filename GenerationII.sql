-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 20, 2020 at 11:44 AM
-- Server version: 10.3.25-MariaDB-0+deb10u1
-- PHP Version: 7.3.19-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Sto`
--

-- --------------------------------------------------------

--
-- Table structure for table `GenerationII`
--

CREATE TABLE `GenerationII` (
  `Word` text NOT NULL,
  `Definition` text NOT NULL,
  `Part of Speech` text NOT NULL,
  `Generation` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `GenerationII`
--

INSERT INTO `GenerationII` (`Word`, `Definition`, `Part of Speech`, `Generation`) VALUES
('daw', 'god; the sun', 'n', 'I'),
('i:i', 'a pearl; any feminine jewel; a gift meant to impart knowledge/seperate epochs', 'n', 'I'),
('dawt', 'to worship', 'v', 'I'),
('dawc', 'a church', 'n', 'I'),
('dawk', 'a temple', 'n', 'I'),
('stodawk', 'a cathedral', 'n', 'I'),
('dawms', 'church trash [slang] ', 'n', 'I'),
('do', 'prayer', 'n', 'I'),
('tantik', 'a redwood; a tree good for lumber', 'n', 'I'),
('tanti:i', 'furniture [general]', 'n', 'I'),
('tanst', 'a small building', 'n', 'I'),
('tami', 'a small dwelling; a hut, shack, small cabin, or tiny home', 'n', 'I'),
('gox', 'a domesticated animal; a four legged furry animal', 'n', 'I'),
('goxt', 'to tame; to be whipped [slang]', 'v', 'I'),
('goa', 'of lower class; cheap', 'adj', 'I'),
('goa', 'a lower class person or animal', 'n', 'I'),
('gost', 'a stuffed animal/animal fetish of personal importance', 'n', 'I'),
('gomi', 'a stuffed animal; any misc toy for a child', 'n', 'I'),
('oxe', 'the idea of a simple part of a human soul/mind', 'n', 'I'),
('ox', 'a beast of burden', 'n', 'I'),
('iest', 'stone; building stone', 'n', 'I'),
('istoith', 'the holy text; a message carved in stone', 'n', 'I'),
('iex', 'stone carved by water or plants', 'n', 'I'),
('iems', 'a pebblle; a small rock; a brick', 'n', 'I'),
('hetik', 'the woods; a wooded area', 'n', 'I'),
('heaw', 'wood defenders; spirit warriors; a member of the military; a soldier', 'n', 'I'),
('hawth', 'land with edible/medicinal plants; a greenhouse; a bontanical garden', 'n', 'I'),
('heipa', 'sustainability', 'n', 'I'),
('heipa', 'sustainable', 'adj', 'I'),
('ipipawx', 'water; a stream; a river; a pond', 'n', 'I'),
('ipia', 'a tool used for carving', 'n', 'I'),
('pipith', 'water in any man made vessle', 'n', 'I'),
('ipioe', 'sentience; someone who lives with awareness', 'n', 'I'),
('poawn', 'an atom; a fundamental substance', 'n', 'I'),
('poawx', 'an ant', 'n', 'I'),
('oawst', 'metal in a workable form', 'n', 'I'),
('poipa', 'a connection [semantic field/ in actions/in values/in worldview]', 'n', 'I'),
('coovooaw', 'a sickness', 'n', 'I'),
('hukawas', 'the earth', 'n', 'I'),
('awoipa', 'energy; the heart; emotion; concentration', 'n', 'I'),
('thuk', 'an edible root', 'n', 'I'),
('poi:i', 'light', 'n', 'I'),
('pik', 'a cure', 'n', 'I'),
('tantoith', 'a tower', 'n', 'I'),
('sheaw', 'bone', 'n', 'I'),
('shuaw', 'spit', 'n', 'I'),
('shucaw', 'skin', 'n', 'I'),
('rawx', 'diurnal life', 'n', 'I'),
('nrawx', 'nocturnal life', 'n', 'I'),
('euc', 'a person', 'n', 'I'),
('eawma', 'the moon; a demon; evil', 'n', 'I'),
('ziet', 'to be', 'v', 'I'),
('oeipa', 'the unexplainable/unknown/intangible parts of life', 'n', 'I'),
('mua', 'jealousy', 'n', 'I'),
('inooi:i', 'skepticism', 'n', 'I'),
('coaipa', 'a promise', 'n', 'I'),
('euaw', 'an eye', 'n', 'I'),
('uaw', 'color', 'n', 'I'),
('tiu', 'reds', 'n', 'I'),
('etiu', 'red', 'n', 'I'),
('uipa', 'blues', 'n', 'I'),
('euipa', 'blue', 'n', 'I'),
('du', 'greens', 'n', 'I'),
('edu', 'green', 'n', 'I'),
('uie', 'black', 'n', 'I'),
('awma', 'white', 'n', 'I'),
('ietiu', 'dark red', 'n', 'I'),
('tiawma', 'light red', 'n', 'I'),
('awmaipa', 'light blue', 'n', 'I'),
('#NAME?', 'like', 'suff', 'I'),
('eawmoo', 'bad; wet; many', 'adj', 'I'),
('doo', 'good; dry; few/singular', 'adj', 'I'),
('tanioo', 'new; small', 'adj', 'I'),
('tikioo', 'old; big; strong', 'adj', 'I'),
('estoo', 'dull; smooth; blunt; east', 'adj', 'I'),
('estoo', 'the east', 'n', 'I'),
('ipioo', 'sharp; pointed; fine; west', 'adj', 'I'),
('ipioo', 'the west', 'n', 'I'),
('hawthoo', 'close; near; calm; south', 'adj', 'I'),
('hawthoo', 'the south', 'n', 'I'),
('hetikoo', 'far; chaotic; north', 'adj', 'I'),
('hetikoo', 'the north', 'n', 'I'),
('ca', 'station; version; form; position; state', 'n', 'I'),
('ipieca', 'ice [lit: stone water]', 'n', 'I'),
('awshimi', 'air', 'n', 'I'),
('ipishica', 'steam [lit: air water]', 'n', 'I'),
('tawmca', 'ash', 'n', 'I'),
('ntan', 'soil; ground; earth; the valley', 'n', 'I'),
('mocashi', 'smoke', 'n', 'I'),
('istoo', 'sand; dust', 'n', 'I'),
('chaw', 'salt', 'n', 'I'),
('soawm', 'salt', 'n', 'I'),
('so', 'salt [root]', 'n', 'I'),
('sot', 'to preserve; to salt; to survive', 'v', 'I'),
('soipat', 'to cry', 'v', 'I'),
('isthawk', 'wooded mountain; jagged mountain', 'n', 'I'),
('ipistuk', 'smooth mountain [i.e. granite]; glacier', 'n', 'I'),
('ipica', 'lake', 'n', 'I'),
('ipix', 'river', 'n', 'I'),
('ipimi', 'standing water; swamp', 'n', 'I'),
('upix', 'body of water big enough for currents/tides', 'n', 'I'),
('ehawtamipa', 'road; path; current; flow', 'n', 'I'),
('bawtawk', 'flora', 'n', 'I'),
('bawk', 'plant [small]', 'n', 'I'),
('awx', 'flower', 'n', 'I'),
('bawx', 'fruit [edible, usually from a tree]', 'n', 'I'),
('bawmi', 'grass; cover crop', 'n', 'I'),
('bawmitawk', 'leaf', 'n', 'I'),
('tanawk', 'bark', 'n', 'I'),
('nbawtawk', 'seed', 'n', 'I'),
('tawk', 'root; branch; stick', 'n', 'I'),
('tantawk', 'tree', 'n', 'I'),
('bawms', 'house plant; small cultivated plant', 'n', 'I'),
('tanaw', 'home', 'n', 'I'),
('dawtanaw', 'sky', 'n', 'I'),
('ndawtanaw', 'fog', 'n', 'I'),
('ipidawtan', 'rain', 'n', 'I'),
('dawmi', 'star', 'n', 'I'),
('awshix', 'wind', 'n', 'I'),
('eawoo', 'night', 'n', 'I'),
('awoo', 'day', 'n', 'I'),
('hawedaw', 'year', 'n', 'I'),
('eudaw', 'the big picture; the meaning of life; peace; purpose; the grand design', 'n', 'I'),
('shepawt', 'to nourish; to heal; to feed; to provide', 'v', 'I'),
('uceu', 'you', 'pn', 'I'),
('diceu', 'yours', 'pn', 'I'),
('usteu', 'me', 'n', 'I'),
('disteu', 'mine', 'pn', 'I'),
('tanak', 'town', 'n', 'I'),
('oehawnak', 'frontier; undiscovered/unexplored land', 'n', 'I'),
('#NAME?', 'need; must; have got to', 'v suff', 'I'),
('ucesteu', 'we [exclusive]', 'pn', 'I'),
('uste', 'we [royal]', 'pn', 'I'),
('dawa', 'right [correct]', 'adj', 'I'),
('#NAME?', 'no', 'suff', 'I'),
('n-', 'not; anti', 'n pre', 'I'),
('n-', 'inverse of verb', 'v pre', 'I'),
('io', 'and', 'conj', 'I'),
('oi', 'or', 'conj', 'I'),
('sti', 'if', 'conj', 'I'),
('di', 'because', 'conj', 'I'),
('en', 'in', 'prep', 'I'),
('awn', 'with', 'prep', 'I'),
('naw', 'at; near', 'prep', 'I'),
('bi', 'this', 'dem', 'I'),
('be', 'that', 'dem', 'I'),
('ji', 'here', 'loc', 'I'),
('je', 'there', 'loc', 'I'),
('uc', 'who', '', 'I'),
('oaw', 'what', '', 'I'),
('cawma', 'how', '', 'I'),
('doth', 'time', 'n', 'I'),
('oth', 'when', '', 'I'),
('ip', 'where', '', 'I'),
('euca', 'twin', 'n', 'I'),
('anusi', 'peace', 'n', 'I'),
('scok', 'any bird', 'n', 'I'),
('ucauct', 'to trade', 'v', 'I'),
('ucaucaw', 'trader', 'n', 'I'),
('ipipawems', 'a rocky creek', 'n', 'I'),
('ntanipi', 'island', 'n', 'I'),
('nawk', 'rose', 'n', 'I'),
('scawk', 'edible bird; hunted bird', 'n', 'I'),
('awmat', 'to say truth; to reveal; to uncover; to lift up', 'v', 'I'),
('gawt', 'to help', 'v', 'I'),
('otchek', 'woodchuck; groundhog', 'n', 'I'),
('awkawx', 'food [semantic field], a piece/unit of food', 'n', 'I'),
('sokaw', 'salted meat [usually jerky]', 'n', 'I'),
('kaw', 'meat [animal]', 'n', 'I'),
('soimoox', 'cold blooded animal [thought to be connected to evil spirits]', 'n', 'I'),
('soimaw', 'salted fish', 'n', 'I'),
('dawima', 'fallen hero; fallen god', 'n', 'I'),
('sto', 'the language of the valley; writing [semantic field]', 'n', 'I'),
('iestoith', 'a proclamation', 'n', 'I'),
('awhawni', 'the low fertile valley [where language originated]; deep fertile valley; something god creates that makes humans feel small', 'n', 'I'),
('ipat', 'to have; to own; to be infected by', 'v', 'II'),
('si', 'showing genetive relationship between two nouns', 'gen', 'II'),
('ax', 'animal hide; animal skin', 'n', 'II'),
('ucox', 'a monkey; a primate', 'n', 'II'),
('ci:i', 'hand', 'n', 'II'),
('ntant', 'to farm', 'v', 'II'),
('po', '[replacement for object in sentences with intransitive verbs]', 'obj', 'II'),
('scot', 'to fly', 'v', 'II'),
('sco', 'insect; any animal that flys that is not a bird', 'n', 'II'),
('eucaw', 'a man', 'n', 'I'),
('eucawn', 'a woman', 'n', 'I'),
('awkawt', 'to eat', 'v', 'I'),
('pawpaw', 'a large green edible fruit native to the City (tastes like mango and banana); in some versions of the creation myth it was given to man as a secret first gift', 'n', 'II'),
('scopix', '(name) river of insects', 'pn', 'II'),
('ieoo', 'sturdy; dependable', 'adj', 'II'),
('pishu', 'berry', 'n', 'II'),
('ieoo', 'dark', 'adj', 'II'),
('dawntik', 'maple tree', 'n', 'II'),
('ti:isco', 'bee', 'n', 'II'),
('ti:i', 'honey', 'n', 'II'),
('dawn', 'maple sugar [grains or syrup]', 'n', 'II'),
('tawn', 'sugar', 'n', 'II'),
('tawnoo', 'sweet', 'adj', 'II'),
('pawx', 'personal water container [how all water was carried; usually made of animal hide]', 'n', 'II'),
('awmi', 'fire', 'n', 'II'),
('tawmith', 'wine', 'n', 'II'),
('ntawna', 'clay', 'n', 'II'),
('tawoo', 'solid [as opposed to liquid and gas]', 'adj', 'II'),
('ntawmi', 'pottery; ceramics', 'n', 'II'),
('ntawnith', 'jug', 'n', 'II'),
('di', 'but', '', 'II'),
('id', 'and', 'conj', 'II');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
