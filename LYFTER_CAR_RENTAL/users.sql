SET search_path TO lyfter_car_rental;

DROP TABLE IF EXISTS users CASCADE;

create table users (
	id SERIAL PRIMARY KEY,
	full_name VARCHAR(50),
	email VARCHAR(50),
	user_name VARCHAR(50),
	password VARCHAR(50),
	birthdate DATE,
	account_status VARCHAR(20) CHECK (account_status IN('regular', 'suspended', 'delinquent'))
);

insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Maxim Tison', 'mtison0@hexun.com', 'mtison0', 'rH1|,WM#O''', '3/21/2026', 'delinquent');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Bordy St. Louis', 'bst1@narod.ru', 'bst1', 'uM1/@j~$,m\e9S', '1/1/2026', 'delinquent');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Hildegarde Pallaske', 'hpallaske2@twitter.com', 'hpallaske2', 'nF6<8|b,', '1/10/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Alexi Andrini', 'aandrini3@360.cn', 'aandrini3', 'bV4@Rf#T\aZIU', '4/15/2026', 'suspended');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Vladamir Barrett', 'vbarrett4@nydailynews.com', 'vbarrett4', 'eQ4#ttbaXSuK`)64', '9/28/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Shana Roach', 'sroach5@mozilla.org', 'sroach5', 'gY7~Ov/GZrF4+', '6/16/2026', 'suspended');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Brigitta Hawkyens', 'bhawkyens6@fema.gov', 'bhawkyens6', 'nG3.1}V~K&!6', '6/24/2026', 'suspended');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Constantin Earney', 'cearney7@quantcast.com', 'cearney7', 'uJ0\w!pm(Uw2emV', '9/8/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Allard Doumerque', 'adoumerque8@dagondesign.com', 'adoumerque8', 'xZ6@t!EeCQGwN', '4/13/2026', 'delinquent');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Gay Eddicott', 'geddicott9@ycombinator.com', 'geddicott9', 'gI8~}TDb''h>)A', '4/2/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Sly Galliver', 'sgallivera@amazon.co.uk', 'sgallivera', 'yX2?>Nvd"', '9/30/2026', 'delinquent');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Kelwin Negri', 'knegrib@sitemeter.com', 'knegrib', 'aD8}<,oI`1{', '12/13/2025', 'suspended');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Quent Leek', 'qleekc@bigcartel.com', 'qleekc', 'kL5\`(A8i', '11/30/2025', 'suspended');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Flor Garces', 'fgarcesd@dyndns.org', 'fgarcesd', 'fJ0?m?w}U~ZU7', '5/5/2026', 'suspended');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Billye Courtese', 'bcourtesee@1688.com', 'bcourtesee', 'dG5/%!fWf3&G.', '3/24/2026', 'suspended');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Nananne Twitchett', 'ntwitchettf@tripod.com', 'ntwitchettf', 'hT6*@%aU}}Z', '9/10/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Shelly Muckloe', 'smuckloeg@yelp.com', 'smuckloeg', 'hS0|Af~}c', '5/15/2026', 'delinquent');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Audrie Tuckwood', 'atuckwoodh@sogou.com', 'atuckwoodh', 'jZ0+N1A1dPGf<', '4/19/2026', 'delinquent');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Noni Steffan', 'nsteffani@vinaora.com', 'nsteffani', 'xV4)vMW9H/', '4/2/2026', 'suspended');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Barbi Groger', 'bgrogerj@intel.com', 'bgrogerj', 'bF6)aoyCz+nF`j', '11/3/2025', 'delinquent');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Lynnet Di Pietro', 'ldik@gnu.org', 'ldik', 'yW9*_H$X1fi@"L', '1/15/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Bernarr Joerning', 'bjoerningl@4shared.com', 'bjoerningl', 'iK1<ii6<t', '5/1/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Egon Daveren', 'edaverenm@domainmarket.com', 'edaverenm', 'rP7@''|~1nrbg3', '4/4/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Felix Bonhan', 'fbonhann@miitbeian.gov.cn', 'fbonhann', 'sF6}dlf0V', '2/15/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Buddie Deesly', 'bdeeslyo@unblog.fr', 'bdeeslyo', 'bX8*HqX<Db!', '10/22/2026', 'delinquent');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Melany Farrance', 'mfarrancep@cornell.edu', 'mfarrancep', 'iZ8+m(R5eEFz5q\r', '2/24/2026', 'delinquent');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Haskel Margery', 'hmargeryq@blinklist.com', 'hmargeryq', 'hJ8+#$syah', '1/10/2026', 'suspended');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Flemming Skull', 'fskullr@cafepress.com', 'fskullr', 'lL8_"E{J|a', '12/30/2025', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Daren Blazeby', 'dblazebys@squidoo.com', 'dblazebys', 'pK3~R&w|K$6!', '10/7/2026', 'suspended');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Mitchael Mungin', 'mmungint@google.cn', 'mmungint', 'tA1?>PHj', '3/12/2026', 'delinquent');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Clint Gilardi', 'cgilardiu@typepad.com', 'cgilardiu', 'hT3{*@<Ux>,v4|,', '7/4/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Dani Easterby', 'deasterbyv@google.es', 'deasterbyv', 'oW2%|h@m@>', '7/6/2026', 'delinquent');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Gloriane Kinglesyd', 'gkinglesydw@bloomberg.com', 'gkinglesydw', 'wG1|#%Xd}D=', '9/21/2026', 'delinquent');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Marja Pleven', 'mplevenx@ucla.edu', 'mplevenx', 'eS1=WBuSs68', '9/24/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Lynnelle Bugler', 'lbuglery@buzzfeed.com', 'lbuglery', 'mY0/66Rlfez4=\BG', '2/18/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Imogene Faulder', 'ifaulderz@nyu.edu', 'ifaulderz', 'lT5,10>v3$4u%5L', '2/20/2026', 'suspended');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Karna Farlane', 'kfarlane10@statcounter.com', 'kfarlane10', 'kF8{?VX_7i5e', '7/22/2026', 'delinquent');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Janel Alexis', 'jalexis11@fc2.com', 'jalexis11', 'lN3&N1ht_5}G/Qcl', '8/7/2026', 'suspended');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Ninetta Le Gall', 'nle12@vistaprint.com', 'nle12', 'aY6''Z/d6mzo', '2/7/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Raychel Ackhurst', 'rackhurst13@netlog.com', 'rackhurst13', 'sB9{+{2?{.y', '2/19/2026', 'delinquent');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Cammy Croose', 'ccroose14@storify.com', 'ccroose14', 'gQ8+|W2OQr8!H', '5/29/2026', 'suspended');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Mozes Charnick', 'mcharnick15@themeforest.net', 'mcharnick15', 'iF8|q+}*xh`', '1/27/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Lynett Lindenboim', 'llindenboim16@nifty.com', 'llindenboim16', 'nO4*)sTgBg', '9/14/2026', 'suspended');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Phip Stratten', 'pstratten17@dell.com', 'pstratten17', 'kT2=##Tx', '12/29/2025', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Ruby Ericsson', 'rericsson18@fema.gov', 'rericsson18', 'hY0<CuzN!D@1QBk', '6/7/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Marcus Giacomello', 'mgiacomello19@huffingtonpost.com', 'mgiacomello19', 'aU7,kf<HHv&F_', '9/26/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Charissa Bonniface', 'cbonniface1a@miibeian.gov.cn', 'cbonniface1a', 'dQ8`<m?nm', '7/24/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Joshia McCrohon', 'jmccrohon1b@imageshack.us', 'jmccrohon1b', 'kJ5<M@YiThM>e', '2/8/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Scotty Morrel', 'smorrel1c@symantec.com', 'smorrel1c', 'kC3{%{O''+`K', '3/3/2026', 'regular');
insert into users (full_name, email, user_name, password, birthdate, account_status) values ('Maybelle Colton', 'mcolton1d@angelfire.com', 'mcolton1d', 'dM3)lB''85u=}7', '5/7/2026', 'regular');
