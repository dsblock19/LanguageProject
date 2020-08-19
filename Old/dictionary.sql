-- MySQL dump 10.17  Distrib 10.3.22-MariaDB, for debian-linux-gnueabihf (armv8l)
--
-- Host: localhost    Database: dictionary
-- ------------------------------------------------------
-- Server version	10.3.22-MariaDB-0+deb10u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `words`
--

DROP TABLE IF EXISTS `words`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `words` (
  `word` text NOT NULL,
  `definition` text NOT NULL,
  `part of speech` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `words`
--

LOCK TABLES `words` WRITE;
/*!40000 ALTER TABLE `words` DISABLE KEYS */;
INSERT INTO `words` VALUES ('daw','god; the sun','n'),('i:i','a pearl; any feminine jewel; a gift meant to impart knowledge/seperate epochs','n'),('dawt','to worship','v'),('dawc','a church','n'),('dawk','a temple','n'),('stodawk','a cathedral','n'),('dawms','(sl) church trash','n'),('do','prayer','n'),('tantik','a redwood; a tree good for lumber','n'),('tanti:i','furniture (gen)','n'),('tanst','a small building','n'),('tami','a small dwelling; a hut, shack, small cabin, or tiny home','n'),('gox','a domesticated animal; a four legged furry animal','n'),('goxt','to tame; to be whipped (sl)','v'),('goa','of lower class; cheap','adj'),('goa','a lower class person or animal','n'),('gost','a stuffed animal/animal fetish of personal importance','n'),('gomi','a stuffed animal; any misc toy for a child','n'),('oxe','the idea of a simple part of a human soul/mind','n'),('ox','a beast of burden','n'),('iest','stone; building stone','n'),('istoith','the holy text; a message carved in stone','n'),('iex','stone carved by water or plants','n'),('iems','a pebblle; a small rock; a brick','n'),('ieo','a sturdy object; a dependable aspect','n'),('ieo','sturdy; dependable','adj'),('hetik','the woods; a wooded area','n'),('heaw','wood defenders; spirit warriors; a member of the military; a soldier','n'),('hawth','land with edible/medicinal plants; a greenhouse; a bontanical garden','n'),('heipa','sustainability','n'),('heipa','sustainable','adj'),('ipipawx','water; a stream; a river; a pond','n'),('ipia','a tool used for carving','n'),('pipith','water in any man made vessle','n'),('ipioe','sentience; someone who lives with awareness','n'),('poawn','an atom; a fundamental substance','n'),('poawx','an ant','n'),('oawst','metal in a workable form','n'),('poipa','a connection (semantic, in actions, in values, in worldview)','n'),('coovooaw','a sickness','n'),('hukawas','the earth','n'),('awoipa','energy; the heart; emotion; concentration','n'),('thuk','an edible root','n'),('poi:i','light','n'),('pik','a cure','n'),('tantoith','a tower','n'),('sheaw','bone','n'),('shuaw','spit','n'),('shucaw','skin','n'),('rawx','diurnal life','n'),('nrawx','nocturnal life','n'),('euc','a person','n'),('eawma','the moon; a demon; evil','n'),('ziet','to be','v'),('oeipa','the unexplainable, unknown, intangible parts of life','n'),('mua','jealousy','n'),('inooi:i','skepticism','n'),('coaipa','a promise','n'),('euaw','an eye','n'),('uaw','color','n'),('tiu','reds','n'),('etiu','red','n'),('uipa','blues','n'),('euipa','blue','n'),('du','greens','n'),('edu','green','n'),('ie','dark','adj'),('ie','the dark','n'),('uie','black','n'),('awma','white','n'),('ietiu','dark red','n'),('tiawma','light red','n'),('awmaipa','light blue','n'),('-oo','like','suff'),('eawmoo','bad; wet; many','adj'),('doo','good; dry; few/singular','adj'),('tanioo','new; small','adj'),('tikioo','old; big; strong','adj'),('estoo','dull; smooth; blunt; east','adj'),('estoo','the east','n'),('ipioo','sharp; pointed; fine; west','adj'),('ipioo','the west','n'),('hawthoo','close; near; calm; south','adj'),('hawthoo','the south','n'),('hetikoo','far; chaotic; north','adj'),('hetikoo','the north','n'),('ca','station; version; form; position; state','n'),('ipieca','ice (lit: stone water)','n'),('awshimi','air','n'),('ipishica','steam (lit: air water)','n'),('awmoo','fire','n'),('tawmca','ash','n'),('ntan','soil; ground; earth; the valley','n'),('mocashi','smoke','n'),('istoo','sand; dust','n'),('chaw','salt','n'),('soawm','salt','n'),('so','salt (root)','n'),('sot','to preserve; to salt; to survive','v'),('soipat','to cry','v'),('isthawk','wooded mountain; jagged mountain','n'),('ipistuk','smooth mountain (i.e. granite); glacier','n'),('ipica','lake','n'),('ipix','river','n'),('ipimi','standing water; swamp','n'),('upix','body of water big enough for currents/tides','n'),('ehawtamipa','road; path; current; flow','n'),('bawtawk','flora','n'),('bawk','plant (small)','n'),('awx','flower','n'),('bawx','fruit (edible, usually from a tree)','n'),('bawmi','grass; cover crop','n'),('bawmitawk','leaf','n'),('tanawk','bark','n'),('nbawtawk','seed','n'),('tawk','root; branch; stick','n'),('tantawk','tree','n'),('bawms','house plant; small cultivated plant','n'),('tanaw','home','n'),('dawtanaw','sky','n'),('ndawtanaw','fog','n'),('ipidawtan','rain','n'),('dawmi','star','n'),('awshix','wind','n'),('eawoo','night','n'),('awoo','day','n'),('hawedaw','year','n'),('eudaw','the big picture; the meaning of life; peace; purpose; the grand design','n'),('shepawt','to nourish; to heal; to feed; to provide','v'),('uceu','you','pn'),('diceu','yours','pn'),('usteu','me','n'),('disteu','mine','pn'),('tanak','town','n'),('oehawnak','frontier; undiscovered/unexplored land','n'),('-ipa','need; must; have got to (V suff)','v suff'),('ucesteu','we (exclusive)','pn'),('uste','we (royal)','pn'),('dawa','right (correct)','adj'),('-na','no','suff'),('n-','not; anti','n pre'),('n-','inverse of verb','v pre'),('io','and','conj'),('oi','or','conj'),('sti','if','conj'),('di','because','conj'),('en','in','prep'),('awn','with','prep'),('naw','at; near','prep'),('bi','this','dem'),('be','that','dem'),('ji','here','loc'),('je','there','loc'),('uc','who',''),('oaw','what',''),('cawma','how',''),('doth','time','n'),('oth','when',''),('ip','where',''),('euca','twin','n'),('anusi','peace','n'),('scok','any bird','n'),('ucauct','to trade','v'),('ucaucaw','trader','n'),('ipipawems','a rocky creek','n'),('ntanipi','island','n'),('nawk','rose','n'),('scawk','edible bird; hunted bird','n'),('awmat','to say truth; to reveal; to uncover; to lift up','v'),('gawt','to help','v'),('otchek','woodchuck; groundhog','n'),('awkawx','food (semantic field), a piece/unit of food','n'),('sokaw','salted meat (usually jerky)','n'),('kaw','meat (animal)','n'),('soimoox','cold blooded animal (thought to be connected to evil spirits)','n'),('soimaw','salted fish','n'),('dawima','fallen hero; fallen god','n');
/*!40000 ALTER TABLE `words` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-20 23:15:36
