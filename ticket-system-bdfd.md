Hi ! Voici un meilleur système de ticket en bdfd !
En cas de problèmes, contacter **kem.rl** sur discord.

VAIRABLES : nom/value
tickets/0
tickets2/
tickets3/


Code 1 :
Langue : BDScript 2
Trigger : !ticket-menu

$nomention
$botTyping

$onlyIf[$guildID!=;You can't use this in DMs!]
$if[$isSlash==true] $defer $endif
$if[$or[$checkUserPerms[$authorID;ban]==true;$checkUserPerms[$authorID;kick]==true;$checkUserPerms[$authorID;managemessages]==true;$checkUserPerms[$authorID;moderatemembers]==true;$checkUserPerms[$authorID;admin]==true]==true]
$var[is_staff;true]
$endif

$if[$var[is_staff]!=true]
$title[Staff only!]
$description[Désolé **$username**, seuls les membres du personnel disposant d'autorisations spéciales sont autorisés à le faire, vous pouvez contacter un membre du personnel pour le faire à votre place.]
$color[#ea003a]
$ephemeral
$stop
$endif

$title[Ticket Setup Menu]
$description[Vous pouvez modifier le message intégré à l'aide du bouton **Configurer l'intégration**, ajouter ou supprimer des panneaux en appuyant sur le bouton **Panneaux de configuration**, et une fois que vous êtes prêt, cliquez simplement sur le bouton vert **Tous prêts** pour envoyer le message. Menu des tickets !]
$addButton[no;tkt_mdl_cfg-$authorID;Setup Embed;primary;no;]
$addButton[no;tkt_add_pnl-$authorID;Setup Ticket Panel(s);secondary;no;]
$addButton[no;tkt_pnl_send-$authorID;Panel Prêt (Envoyer);success;no;]
$setChannelVar[tickets2;]
$setChannelVar[tickets3;]
$setChannelVar[tickets;]
$color[#1874cb]
$suppressErrors


Code 2 :
Langue : BDScript 2
Trigger : !ticket-config

$nomention
$botTyping 

$onlyIf[$guildID!=;You can't use this in DMs!]
$if[$isSlash==true] $defer $endif

$if[$isAdmin[$authorID]==false]
$title[Admins only!]
$description[Sorry **$username[$authorID]**, Tu n'a pas les permissions pour utiliser cette commande.]
$color[#ea003a]
$ephemeral
$stop
$endif

$color[#1874cb]
$title[Ticket Config Setup]
$description[Salut **$username[$authorID]** ! Vous pouvez configurer certains aspects du système de tickets en utilisant les boutons ci-dessous.]
$addField[Paramètres Généraux;Cette zone vous permet de personnaliser les paramètres généraux, notamment l'heure de fermeture, la catégorie du ticket et les options de notation.]
$addField[Paramètres Rôle;Vous pouvez désigner jusqu'à trois rôles personnels ou sur liste noire dans cette zone, les valeurs précédentes sont remplacées par celles que vous fournissez.]
$addField[Paramètres Embed Message;Vous pouvez customisez le message qui apparaîtra dans le ticket créé.]
$addButton[no;tkt_mdl_gnrl;Paramètres Généraux;primary;no;]
$addButton[no;tkt_mdl_rls;Paramètres Rôle;secondary;no;]
$addButton[no;tkt_mdl_emd;Paramètres Embed Message;secondary;no;]
$if[$isSlash==true]
$ephemeral
$endif
$suppressErrors


Code 3 : 
Langue : BDScript 2
Trigger : !ticket-stats

$nomention
$botTyping

$if[$isSlash==true] $defer $endif
$onlyIf[$guildID!=;You can't use this in DMs!]


$textSplit[$getServerVar[tickets2;$guildID];--]
$enableDecimals[yes]
$if[$isNumber[$splitText[2]]==true]
$var[a;$splitText[1]]
$var[b;$splitText[2]]
$var[c;$splitText[3]]
$var[d;$splitText[4]]
$var[e;$splitText[5]]
$else
$var[a;0] $var[b;0] $var[c;0] $var[d;0] $var[e;0]
$endif
$var[sum;$sum[$var[a];$var[b];$var[c];$var[d];$var[e]]]
$try $var[p_verybad;$round[$multi[$divide[$var[a];$var[sum]];100]]] $catch $var[p_verybad;0] $endtry
$try $var[p_bad;$round[$multi[$divide[$var[b];$var[sum]];100]]] $catch $var[p_bad;0] $endtry
$try $var[p_regular;$round[$multi[$divide[$var[c];$var[sum]];100]]] $catch $var[p_regular;0] $endtry
$try $var[p_good;$round[$multi[$divide[$var[d];$var[sum]];100]]] $catch $var[p_good;0] $endtry
$try $var[p_verygood;$round[$multi[$divide[$var[e];$var[sum]];100]]] $catch $var[p_verygood;0] $endtry

$var[negative;:red_square:]
$var[regular;:blue_square:]
$var[positive;:green_square:]
$var[white;:white_large_square:]

$try $var[pl_verybad;$round[$multi[$divide[$var[a];$var[sum]];10]]] $catch $var[pl_verybad;0] $endtry
$try $var[pl_bad;$round[$multi[$divide[$var[b];$var[sum]];10]]] $catch $var[pl_bad;0] $endtry
$try $var[pl_regular;$round[$multi[$divide[$var[c];$var[sum]];10]]] $catch $var[pl_regular;0] $endtry
$try $var[pl_good;$round[$multi[$divide[$var[d];$var[sum]];10]]] $catch $var[pl_good;0] $endtry
$try $var[pl_verygood;$round[$multi[$divide[$var[e];$var[sum]];10]]] $catch $var[pl_verygood;0] $endtry

$if[$sum[$var[a];$var[b]]>$sum[$var[d];$var[e]]]
$color[#dd2e44]
$else
$color[#78b159]
$endif

$author[$serverName[$guildID]]
$authorIcon[$serverIcon[$guildID]]
$description[
> **$numberSeparator[$getServerVar[tickets]]** tickets ont été créés sur ce serveur !
> **$numberSeparator[$sum[$var[a];$var[b];$var[c];$var[d];$var[e]]]** Critiques totales ! **$numberSeparator[$sum[$var[c];$var[d];$var[e]]]** positifs, **$numberSeparator[$sum[$var[a];$var[b]]]** négatifs!
$addField[Very bad — $numberSeparator[$var[a]];$repeatMessage[$var[pl_verybad];$var[negative]]$repeatMessage[$sub[10;$var[pl_verybad]];$var[white]] **$var[p_verybad]%**;no]
$addField[Bad — $numberSeparator[$var[b]];$repeatMessage[$var[pl_bad];$var[negative]]$repeatMessage[$sub[10;$var[pl_bad]];$var[white]] **$var[p_bad]%**;no]
$addField[Regular — $numberSeparator[$var[c]];$repeatMessage[$var[pl_regular];$var[regular]]$repeatMessage[$sub[10;$var[pl_regular]];$var[white]] **$var[p_regular]%**;no]
$addField[Good — $numberSeparator[$var[d]];$repeatMessage[$var[pl_good];$var[positive]]$repeatMessage[$sub[10;$var[pl_good]];$var[white]] **$var[p_good]%**;no]
$addField[Very good — $numberSeparator[$var[e]];$repeatMessage[$var[pl_verygood];$var[positive]]$repeatMessage[$sub[10;$var[pl_verygood]];$var[white]] **$var[p_verygood]%**;no]
]
$footer[Executé par $username[$authorID]#$discriminator[$authorID]]
$suppressErrors


Code 4 :
Langue : BDScript 2
Trigger : $onInteraction

$nomention
$suppressErrors
                     $c[ ... system configuration, read the comments. ]
                     $c[ ... button emojis, "true" to keep them enabled, "false" to disable them. ]
$var[emojis;true]

$c[ ... Below you can change button emojis to any desired emojis from your keyboard, such as 🔒. Do not use Discord emoji names like :lock: ]

$if[$var[emojis]==true]
$var[solved_emoji;💾]
$var[close_emoji;🔒]
$var[open_emoji;🔓]
$var[sticky_emoji;🗃️]
$var[claim_emoji;🙋‍♂️]
$var[info_emoji;🪪]
$var[back_to_panel_emoji;◀️]
$var[panel_emoji;🛠️]
$var[openticket_emoji;🎫]
$endif

                     $c[ ... general configuration ]
$c[
if you want to know what each setting below do then check this table, do not change these settings without reading first, or it may lead to errors.
https://i.imgur.com/2qEwMVN.png
]
$var[newticket_ping;true] 
$var[branding;true] 
$var[hide_on_sticky;true]
$var[webhook;true]
$var[webhook_default_subject;Hey {user}, how can we help you today?]
$var[always_guild;false]
$var[rating;true]
$var[panel_limit;7] $c[number from scale 1-7]
$var[default_image;https://i.imgur.com/AZlgvgi.png] $c[ <== max. 37 characters URL ]
$c[ ...  Make sure the hexcode colors you provide are valid to avoid errors. ]
$var[main_color;#1874cb]
$var[neutral_color;#faa81a]
$var[success_color;#08b278]
$var[error_color;#ea003a]

$var[rt_msg;To help **{server}** improve their support ticket experience we would like to receive your anonymous feedback.]
$var[rt_footer;How would you rate the support received?] 
$var[negative_rate;Sorry to hear that! Thank you for **rating** this server's ticket support experience, your feedback **helps** ``{server}`` **improve** your support experience, we truly **appreciate** your honesty.]
$var[positive_rate;Glad to hear that! Thank you for **rating** this server's ticket support experience, your feedback **helps** ``{server}`` **improve** your support experience, we truly **appreciate** your feedback.]

$c[ ... Error message that appears when a user don't have enough permissions to use a button. ]
$var[sf_title;Staff only!]
$var[sf_descr;Sorry, only staff members with special permissions are allowed to do this, you can contact a staff member to do it for you.]

$c[ Close ticket button timer, maximal value is 2400 seconds, I just recommend to not touch, time must be in seconds only. ]
$var[close_in;120]

 $c[
 ... Unless you understand the entire system, do not edit the code infrastructure below. You can translate it, but make sure not to remove or edit the name of any function.
]

$var[ticket_message_default;
Hello **{username}**, this is your ticket!
Please, write down below details about your problem. Support will be with you shortly!

You are allowed to ping a support member once after 30 minutes of no response, avoid mass-pinging!

You can close this ticket at anytime by using the **close** button.
Staff can manage this ticket by using the **panel** button.
]

$if[$checkContains[$message;tkt_mdl_o-]==true]
$stop
$endif
$if[$checkContains[$customID;tkt_mdl_op-]==true]
$stop
$endif

$if[$checkContains[$customID;tkt]==true]
$if[$checkContains[$customID;mdl]==false]
$defer
$endif
$endif
$if[$getUserVar[tickets2;$botID]!=]
$textSplit[$getUserVar[tickets2;$botID];-]
$if[$serverChannelExists[$splitText[1]]==true] $var[category;$splitText[1]] $endif
$if[$serverChannelExists[$splitText[2]]==true] $var[logs;$splitText[2]] $endif
$if[$isNumber[$splitText[3]]==true] $var[close_in;$splitText[3]] $endif
$if[$isBoolean[$splitText[4]]==true] $var[rating;$splitText[4]] $endif
$if[$isBoolean[$splitText[5]]==true] $var[webhook;$splitText[5]] $endif
$endif
$textSplit[$getUserVar[tickets3;$botID];≈]
$if[$splitText[1]==] $var[ticket_title;New Ticket!] $else $var[ticket_title;$splitText[1]] $endif
$if[$splitText[2]==]
$var[ticket_message;$var[ticket_message_default]]
$else
$var[ticket_message;$splitText[2]]
$endif
$if[$isValidHex[$splitText[3]]==false]
$var[color;$var[main_color]]
$else
$var[color;$splitText[3]]
$endif
$if[$checkContains[$splitText[4];.png;.jpg;.jpeg;.gif;.webp]==false]
$var[s_image;https://i.imgur.com/YxlQphp.png]
$else
$var[s_image;$splitText[4]]
$endif
$if[$var[branding]==true]
$var[s_thumbnail;https://i.imgur.com/IlZ2w9w.png]
$endif
$textSplit[$getServerVar[tickets3];-]
$var[ts1;$splitText[1]]
$var[ts2;$splitText[2]]
$textSplit[$var[ts1];,]
$try $var[has_staff;$hasRole[$authorID;$splitText[1]]] $endtry
$if[$var[has_staff]!=true]
$try $var[has_staff;$hasRole[$authorID;$splitText[2]]] $endtry
$endif
$if[$var[has_staff]!=true]
$try $var[has_staff;$hasRole[$authorID;$splitText[3]]] $endtry
$endif
$textSplit[$var[ts2];,]
$try $var[is_blacklisted;$hasRole[$authorID;$splitText[1]]] $var[black_role;<@&$splitText[1]>] $endtry
$if[$var[is_blacklisted]!=true]
$try $var[is_blacklisted;$hasRole[$authorID;$splitText[2]]] $var[black_role;<@&$splitText[2]>] $endtry
$endif
$if[$var[is_blacklisted]!=true]
$try $var[is_blacklisted;$hasRole[$authorID;$splitText[3]]] $var[black_role;<@&$splitText[3]>] $endtry
$endif
$if[$var[rating]!=true]
$var[rt_msg;]
$var[rt_footer;]
$endif
$if[$var[has_staff]!=true]
$if[$or[$checkUserPerms[$authorID;ban]==true;$checkUserPerms[$authorID;kick]==true;$checkUserPerms[$authorID;managemessages]==true;$checkUserPerms[$authorID;moderatemembers]==true;$checkUserPerms[$authorID;admin]==true]==true]
$var[is_staff;true]
$else
$var[is_staff;false]
$endif
$else
$var[is_staff;true]
$endif
$if[$checkContains[$customID;tkt_actop-]==true]
$removeButtons
$defer
$if[$var[is_blacklisted]==true]
$title[You can't create tickets!]
$description[Hi **$username[$authorID]**! Unfortunately, one of your roles ($var[black_role]) has been restricted from creating new tickets. If you believe this is a mistake, contact a server manager to have the role removed from the ticket setup command.]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$textSplit[$customID;-]
$var[index;$splitText[2]]
$var[subject;$input[subject]]
$if[$charCount[$replaceText[$var[index];0;;1]]>1]
$var[topic_msg;
**Ticket Panel**
```$cropText[$var[index];$sub[$charCount[$var[index]];2];]```]
$endif
$if[$optOff[$serverChannelExists[$getUserVar[tickets2;$authorID]]]==true]
$if[$checkContains[$channelName[$getUserVar[tickets2]];solved-]==false]
$description[**$username[$authorID]** You already have an open ticket! Please move to your active ticket <#$getUserVar[tickets2]> instead.]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$endif
$var[subject;$cropText[$var[subject];400;(...)]]
$if[$var[subject]==]
$var[subject;No subject was provided by the user.]
$var[subject_empty;true]
$else
$var[subject_empty;false]
$endif
$var[channel_description;Ticket opened by **$username[$authorID]#$discriminator[$authorID]** <t:$getTimestamp:R> (<t:$getTimestamp:F>)]
$var[ticket_message;$replaceText[$var[ticket_message];{username};$username[$authorID];-1]]
$var[format;ticket-{number}]
$if[$isNumber[$getServerVar[tickets]]==false]
$setServerVar[tickets;0]
$endif
$var[tickets;$sum[$getServerVar[tickets];1]]
$if[$charCount[$var[tickets]]==1]
$var[num;000$var[tickets]]
$endif
$if[$charCount[$var[tickets]]==2]
$var[num;00$var[tickets]]
$endif
$if[$charCount[$var[tickets]]==3]
$var[num;0$var[tickets]]
$endif
$if[$charCount[$var[tickets]]>3]
$var[num;$var[tickets]]
$endif
$var[username_format;$replaceText[$replaceText[$url[encode;$cropText[$username[$authorID];7;]];-;;-1];%;;-1]]
$var[name;$replaceText[$replaceText[$replaceText[$replaceText[$var[format];{number};$var[num];1];{username};$var[username_format];1];{random_number};$random[10000;99999];-1];{discriminator};$discriminator[$authorID];-1]]
$if[$charCount[$var[category]]>14]
$createChannel[$var[name];text;$var[category]]
$else
$createChannel[$var[name];text]
$endif
$setServerVar[tickets;$sum[$getServerVar[tickets];1]]
$var[new_ticket;$findChannel[$var[name]]]
$var[success_open;<@$authorID> tu as créé le ticket <#$var[new_ticket]> !]
$description[$var[success_open]]
$color[$var[success_color]]
$ephemeral
$setChannelVar[tickets;$authorID;$var[new_ticket]]
$setUserVar[tickets2;$var[new_ticket]]
$modifyChannel[$var[new_ticket];!unchanged;$var[channel_description];false;!unchanged;!unchanged]
$textSplit[$getServerVar[tickets3];-]
$var[ts1;$splitText[1]]
$var[ts2;$splitText[2]]
$textSplit[$var[ts1];,]
$if[$roleExists[$splitText[1]]==true] $try $editChannelPerms[$var[new_ticket];$splitText[1];+sendmessages;+readmessages;+embedlinks;+attachfiles] $endtry $endif
$if[$roleExists[$splitText[2]]==true] $try $editChannelPerms[$var[new_ticket];$splitText[2];+sendmessages;+readmessages;+embedlinks;+attachfiles] $endtry $endif
$if[$roleExists[$splitText[3]]==true] $try $editChannelPerms[$var[new_ticket];$splitText[3];+sendmessages;+readmessages;+embedlinks;+attachfiles] $endtry $endif
$editChannelPerms[$var[new_ticket];$guildID;-readmessages]
$editChannelPerms[$var[new_ticket];$authorID;+sendmessages;+readmessages;+embedlinks;+attachfiles]
$useChannel[$var[new_ticket]]
$try
$if[$var[newticket_ping]==true]
$var[ping_id;$sendMessage[<@$authorID>;yes]]
$deleteMessage[$var[new_ticket];$var[ping_id]]
$endif
$endtry
$if[$isValidHex[$var[color]]==false]
$var[color;$var[main_color]]
$endif
$async[logs_block]
$if[$serverChannelExists[$var[logs]]]
$try
$sendEmbedMessage[$var[logs];;New Ticked Created!;;Ticket ``#$channelName[$var[new_ticket]]`` (<#$var[new_ticket]>) has been **created** by <@$authorID> (**$username[$authorID]#$discriminator[$authorID]**)!
**Sujet :**
```$var[subject]```
;$var[main_color];;;;;;;;no]
$endtry
$endif
$endasync
$var[res_id;$sendEmbedMessage[$var[new_ticket];
;$var[ticket_title]
;$getBotInvite
;$var[ticket_message]$var[topic_msg]
**Sujet du Ticket :**
```$var[subject]```
;$var[color]
;$username[$authorID]#$discriminator[$authorID]
;$userAvatar[$authorID];;;$var[s_thumbnail]
;$var[s_image]
;no
;yes]]
$addButton[no;tkt_close;Close Ticket;danger;no;$var[close_emoji];$var[res_id]]
$addButton[no;tkt_pnel;Staff Panel;primary;no;$var[panel_emoji];$var[res_id]]
$if[$var[webhook]==true]
$try
$if[$and[$var[subject_empty]==false;$var[always_guild]==false]==true]
$var[webhookURL;$webhookCreate[$var[new_ticket];$username[$authorID];$userAvatar[$authorID]]]
$webhookAvatarURL[$var[webhookURL];$userAvatar[$authorID]]
$webhookContent[$var[webhookURL];$var[subject]]
$else
$var[webhookURL;$webhookCreate[$var[new_ticket];$serverName[$guildID];$serverIcon[$guildID]]]
$webhookAvatarURL[$var[webhookURL];$serverIcon[$guildID]]
$webhookContent[$var[webhookURL];$replaceText[$var[webhook_default_subject];{user};<@$authorID>;-1]]
$endif
$endtry
$endif
$stop $c[s]
$endif
$if[$customID==tkt_mdl_emd]
$if[$or[$var[is_staff]==false;$checkUserPerms[$authorID;manageserver]==false]==true]
$removeButtons
$title[$var[sf_title]]
$description[$var[sf_descr]]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$textSplit[$getUserVar[tickets3;$botID];≈]
$if[$splitText[1]==] $var[e_title;New Ticket!] $else $var[e_title;$splitText[1]] $endif
$if[$splitText[2]==] $var[e_desc;$var[ticket_message]] $else $var[e_desc;$splitText[2]] $endif
$if[$splitText[3]==] $var[e_color;$var[main_color]] $else $var[e_color;$splitText[3]] $endif
$if[$splitText[4]==] $var[e_image;$var[s_image]] $else $var[e_image;$splitText[4]] $endif
$newModal[tkt_emdset;Embed Settings]
$addTextInput[embed_title;short;Embed Title;1;50;no;$var[e_title];Embed title, leave it empty to use the default one.]
$addTextInput[embed_description;paragraph;Embed Description;1;500;no;$var[e_desc];Embed description, leave it empty to use the default one, you can use the {username} placeholder.]
$addTextInput[embed_color;short;Embed Color;6;7;no;$var[e_color];Embed color hexcode, leave it empty to use the default one.]
$addTextInput[embed_image;short;Embed Bottom Image URL;5;100;no;$var[e_image];Embed bottom image URL, leave it empty to use the default one.]
$endif
$if[$customID==tkt_emdset]
$var[pf;0]
$if[$input[embed_color]!=]
$if[$isValidHex[$input[embed_color]]==false]
$var[problems;$var[problems] The embed color hexcode you gave is not valid or I can't recognize it as valid, try using a Hexcode Color Picker online. ]
$var[pf;$sum[$var[pf];1]]
$endif
$endif
$if[$input[embed_image]!=]
$if[$checkContains[$input[embed_image];.png;.jpg;.webp;.gif;.jpeg]==false]
$var[problems;$var[problems] The embed image URL you gave is not valid or I can't recognize it as valid, valid image URLs ends with the image extension such as .jpg, .png, and so on, you can try to upload the image to Discord, copying the link and using it. ]
$var[pf;$sum[$var[pf];1]]
$endif
$endif
> :ballot_box_with_check: *This is a preview, you can dismiss it, **$var[pf]** problems found, **changes saved successfully**.*
$if[$var[pf]>0]
$var[ind;2]
$author[Problems Found;1]
$description[```$replaceText[$replaceText[$var[problems]; ;;1];  ; & ;-1]```;1]
$color[$var[error_color];1]
$else
$var[ind;1]
$endif
$if[$input[embed_title]!=]
$title[$input[embed_title];$var[ind]]
$else
$title[New Ticket!;$var[ind]]
$endif
$embeddedURL[$getBotInvite;$var[ind]]
$if[$input[embed_description]!=]
$description[$replaceText[$input[embed_description];{username};$username[$authorID];-1];$var[ind]]
$else
$description[$replaceText[$var[ticket_message_default];{username};$username[$authorID];-1];$var[ind]]
$endif
$addField[Ticket Panel;```Panel Name would go here.```;no;$var[ind]]
$addField[Ticket Subject;```Ticket Subject would go here.```;no;$var[ind]]
$try $thumbnail[$var[s_thumbnail];$var[ind]] $endtry
$if[$input[embed_image]!=]
$try $image[$input[embed_image];$var[ind]] $catch $try $image[$var[s_image];$var[ind]] $endtry $endtry
$else
$try $image[$var[s_image];$var[ind]] $endtry
$endif
$if[$input[embed_color]!=]
$try $color[$input[embed_color];$var[ind]] $catch $try $color[$var[main_color];$var[ind]] $endtry $endtry
$else
$try $color[$var[main_color];$var[ind]] $endtry
$endif
$try
$setUserVar[tickets3;$replaceText[$input[embed_title];≈;~;-1]≈$replaceText[$input[embed_description];≈;~;-1]≈$replaceText[$input[embed_color];≈;~;-1]≈$replaceText[$input[embed_image];≈;~;-1];$botID]
$catch
> :x: *There has been an error trying to save the embed data correctly, please contact a Developer.*
$endtry
$ephemeral
$stop $c[s]
$endif
$if[$customID==tkt_mdl_gnrl]
$if[$or[$var[is_staff]==false;$checkUserPerms[$authorID;manageserver]==false]==true]
$removeButtons
$title[$var[sf_title]]
$description[$var[sf_descr]]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$textSplit[$getUserVar[tickets2;$botID];-]
$if[$splitText[3]==] $var[split3;$var[close_in]] $else $var[split3;$splitText[3]] $endif
$if[$splitText[4]==] $var[split4;$var[rating]] $else $var[split4;$splitText[4]] $endif
$if[$splitText[5]==] $var[split5;$var[webhook]] $else $var[split5;$splitText[5]] $endif
$newModal[tkt_gnrlset;General Settings]
$addTextInput[category;short;New Tickets Category;1;50;no;$splitText[1];Category ID or name, where tickets will be created.]
$addTextInput[logschannel;short;Ticket Logs Channel;1;50;no;$splitText[2];Channel ID or name, where I will log closed/opened tickets.]
$addTextInput[closein;short;Close Button Time (in seconds);1;5;no;$var[split3]s;There's a timer in the Close Ticket button, value in SECONDS for that timer.]
$addTextInput[rating;short;Should Rating be enabled?;2;5;no;$var[split4];Yes/no or true/false, should the users be able to rate?]
$addTextInput[webhooks;short;Should Webhooks be enabled?;2;5;no;$var[split5];Yes/no or true/false, should I send a webhook message in new tickets?]
$endif
$if[$customID==tkt_mdl_rls]
$if[$or[$var[is_staff]==false;$checkUserPerms[$authorID;manageserver]==false]==true]
$removeButtons
$title[$var[sf_title]]
$description[$var[sf_descr]]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$textSplit[$getServerVar[tickets3];-]
$var[current_sr;$splitText[1]]
$var[current_br;$splitText[2]]
$newModal[tkt_rlsset;Role Settings]
$addTextInput[staffroles;short;Staff Role(s) (Max 3 roles);1;55;no;$var[current_sr];Role(s) name, ID or mention, separable using commas.]
$addTextInput[blacklistedroles;short;Blacklisted Role(s) (Max 3 roles);1;55;no;$var[current_br];Role(s) name, ID or mention, separable using commas.]
$endif
$if[$customID==tkt_mdl_cfg-$authorID]
$if[$or[$var[is_staff]==false;$checkUserPerms[$authorID;manageserver]==false]==true]
$stop
$endif
$newModal[tkt_cfg-$authorID;Embed Customization]
$addTextInput[ticket-title;short;Embed Title;1;40;yes;;Any Title you want to show in the embed here, required.]
$addTextInput[ticket-description;paragraph;Embed Description;1;300;yes;;Any Description you want to show in the embed here, required.]
$addTextInput[ticket-footer;short;Embed Footer;0;50;no;;Any Footer you want to show in the embed here, optional.]
$addTextInput[ticket-color;short;Embed Color Hexcode;6;7;no;;Any color hexcode (e.x "ffffff") or leave it empty, optional.]
$addTextInput[ticket-image;short;Embed Image URL;1;32;no;$var[default_image];Any image URL or leave it empty to use default one, optional.]
$endif
$if[$customID==tkt_pnlact_mdl_add-$authorID]
$if[$or[$var[is_staff]==false;$checkUserPerms[$authorID;manageserver]==false]==true]
$removeButtons
$title[$var[sf_title]]
$description[$var[sf_descr]]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$textSplit[$getChannelVar[tickets];≈]
$var[l;$getTextSplitLength]
$if[$var[l]>$var[panel_limit]]
$removeButtons
$description[You cannot create another Ticket Panel, there's a limit of **$var[panel_limit]** panels! You can either remove a panel or create another ticket menu.]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$newModal[tkt_pnlact_add-$authorID;Create new panel]
$addTextInput[paneltitle;short;Panel Title;1;20;yes;;Title here (ex. "General Support")]
$addTextInput[paneldescription;short;Panel Description;1;40;yes;;Description here (ex. "Get general support")]
$endif
$if[$customID==tkt_pnlact_mdl_edit-$authorID]
$removeButtons
$if[$or[$var[is_staff]==false;$checkUserPerms[$authorID;manageserver]==false]==true]
$removeButtons
$title[$var[sf_title]]
$description[$var[sf_descr]]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$newModal[tkt_pnlact_edit-$authorID;Edit an existing panel]
$addTextInput[panelid;short;Panel ID;1;1;yes;;ID here (ex. "2")]
$addTextInput[paneltitle;short;New Panel Title;1;20;no;;Leave it empty to use the old Title!]
$addTextInput[paneldescription;short;New Panel Description;1;40;no;;Leave it empty to use the old Description!]
$ephemeral
$endif
$if[$customID==tkt_gnrlset]
$var[pf;0]
$if[$input[logschannel]!=]
$var[logs_channel;$findChannel[$input[logschannel]]]
$endif
$if[$input[category]!=]
$var[ticket_category;$findChannel[$input[category]]]
$endif
$if[$and[$var[ticket_category]==;$input[category]!=]==true]
$var[ticket_category;01000010011001010111001001101011]
$endif
$if[$and[$var[logs_channel]==;$input[logschannel]!=]==true]
$var[logs_channel;07082004]
$endif
$var[close_in;$replaceText[$input[closein];s;;-1]]
$if[$input[webhooks]!=]
$if[$isBoolean[$input[webhooks]]==true]
$if[$checkContains[$toLowercase[$input[webhooks]];true;yes]==true]
$addField[Webhooks;```Enabled ($input[webhooks])```;yes]
$var[input_webhooks;true]
$else
$addField[Webhooks;```Disabled ($input[webhooks])```;yes]
$var[input_webhooks;false]
$endif
$else
$var[problems;$var[problems] The value you gave for the "Webhooks" option is invalid, it must be yes/no, or true/false. ]
$var[pf;$sum[$var[pf];1]]
$endif
$endif
$if[$input[rating]!=]
$if[$isBoolean[$input[rating]]==true]
$if[$checkContains[$toLowercase[$input[rating]];true;yes]==true]
$addField[Rating System;```Enabled ($input[rating])```;yes]
$var[input_rating;true]
$else
$addField[Rating System;```Disabled ($input[rating])```;yes]
$var[input_rating;false]
$endif
$else
$var[problems;$var[problems] The value you gave for the "Rating" option is invalid, it must be yes/no, or true/false. ]
$var[pf;$sum[$var[pf];1]]
$endif
$endif
$if[$var[close_in]!=]
$if[$isNumber[$var[close_in]]==true]
$if[$var[close_in]>2400]
$var[problems;$var[problems] The value you gave for the "Button Closing Time" must be a number between 5 and 2400, the maximum is 2400 seconds (40 minutes), you can't exceed it. ]
$var[pf;$sum[$var[pf];1]]
$else
$if[$var[close_in]>4]
$if[$var[close_in]>60]
$var[humanized;$divide[$var[close_in];60] minutes]
$else
$var[humanized;$var[close_in] seconds]
$endif
$addField[Close Button Timer;```$var[humanized] ($var[close_in] seconds)```;yes]
$var[input_closein;$var[close_in]]
$else
$var[problems;$var[problems] The value you gave for the "Button Closing Time" must be a number between 5 and 2400, the minimum is 5 seconds. ]
$var[pf;$sum[$var[pf];1]]
$endif
$endif
$else
$var[problems;$var[problems] The value you gave for the "Button Closing Time" option was not a number, please make sure to provide a valid number in SECONDS to represent the button close timer, such as "120" for 2 minutes. ]
$var[pf;$sum[$var[pf];1]]
$endif
$endif
$if[$var[logs_channel]!=]
$try
$var[logstype;$channelType[$var[logs_channel]]]
$endtry
$if[$var[logstype]==text]
$if[$serverChannelExists[$var[logs_channel]]==true]
$addField[Ticket Logs Channel;<#$var[logs_channel]>;yes]
$var[input_logs;$var[logs_channel]]
$else
$var[problems;$var[problems] Invalid Ticket Logs Channel name/ID given, it must be a channel from this server! ]
$var[pf;$sum[$var[pf];1]]
$endif
$else
$var[problems;$var[problems] Invalid Ticket Logs Channel name/ID given, if you used a name try with an ID and viceversa, make sure the ID is right! ]
$var[pf;$sum[$var[pf];1]]
$endif
$endif
$if[$var[ticket_category]!=]
$try
$var[cattype;$channelType[$var[ticket_category]]]
$endtry
$if[$var[cattype]==category]
$if[$serverChannelExists[$var[ticket_category]]==true]
$addField[Tickets Category;<#$var[ticket_category]>;yes]
$var[input_category;$var[ticket_category]]
$else
$var[problems;$var[problems] Invalid Ticket Category name/ID given, it must be a category from this server! ]
$var[pf;$sum[$var[pf];1]]
$endif
$else
$var[problems;$var[problems] Invalid Ticket Category name/ID given, if you used a name try with an ID and viceversa, make sure the ID is right! ]
$var[pf;$sum[$var[pf];1]]
$endif
$endif
$color[$var[success_color]]
$title[Success!]
$description[> **$var[pf]** problems found! Changes has been applied successfully.]
$setUserVar[tickets2;$var[input_category]-$var[input_logs]-$var[input_closein]-$var[input_rating]-$var[input_webhooks];$botID]
$if[$var[pf]>0]
$addField[Problems Found;```$replaceText[$replaceText[$var[problems]; ;;1];  ; & ;-1]```]
$endif
$ephemeral
$stop $c[s]
$endif
$if[$customID==tkt_rlsset]
$if[$input[staffroles]!=]
$textSplit[$replaceText[$replaceText[$replaceText[$input[staffroles];<;;-1];>;;-1];@&;;-1];,]
$if[$roleExists[$findRole[$splitText[1]]]==true]
$var[sr;$findRole[$splitText[1]]]
$var[sr1;$findRole[$splitText[1]]]
$endif
$if[$getTextSplitLength>1]
$if[$roleExists[$findRole[$splitText[2]]]==true]
$var[sr;$var[sr] $findRole[$splitText[2]]]
$var[sr2;$findRole[$splitText[2]]]
$endif
$endif
$if[$getTextSplitLength>2]
$if[$roleExists[$findRole[$splitText[3]]]==true]
$var[sr;$var[sr] $findRole[$splitText[3]]]
$var[sr3;$findRole[$splitText[3]]]
$endif
$endif
$if[$and[$roleExists[$var[sr1]]==false;$roleExists[$var[sr2]]==false;$roleExists[$var[sr3]]==false]==true]
$var[failed;true]
$var[failed_error;Invalid roles given in "Staff Roles"! Try using role IDs separated by comma instead.]
$endif
$var[sr;$replaceText[$var[sr];  ;;-1]]
$var[sr;$replaceText[$var[sr];  ;;-1]]
$var[sr;$replaceText[$var[sr]; ;,;-1]]
$textSplit[$var[sr];,]
$var[sr_n;0]
$if[$roleExists[$splitText[1]]==true] $var[sr_n;$sum[$var[sr_n];1]] $endif
$if[$roleExists[$splitText[2]]==true] $var[sr_n;$sum[$var[sr_n];1]] $endif
$if[$roleExists[$splitText[3]]==true] $var[sr_n;$sum[$var[sr_n];1]] $endif
$var[sr_length;$var[sr_n]]
$if[$var[sr_length]>1]
$var[sr_msg;<@&$splitText[1]>
<@&$splitText[2]>]
$var[sr_plural;s]
$else
$var[sr_msg;<@&$splitText[1]>]
$endif
$if[$var[sr_length]>2]
$var[sr_msg;$var[sr_msg]
<@&$splitText[3]>]
$endif
$if[$checkContains[$var[sr_msg];<@&>]==true]
$var[failed;true]
$var[failed_error;Please use only one role value (ID, name, or mention) when specifying roles. Combining multiple values may cause errors. If you are using only one role, try using its ID. If the problem persists, contact a bot developer, this error comes from the "Staff Roles" input.]
$endif
$endif
$if[$input[blacklistedroles]!=]
$textSplit[$replaceText[$replaceText[$replaceText[$input[blacklistedroles];<;;-1];>;;-1];@&;;-1];,]
$if[$roleExists[$findRole[$splitText[1]]]==true]
$var[br;$findRole[$splitText[1]]]
$var[br1;$findRole[$splitText[1]]]
$endif
$if[$getTextSplitLength>1]
$if[$roleExists[$findRole[$splitText[2]]]==true]
$var[br;$var[br] $findRole[$splitText[2]]]
$var[br2;$findRole[$splitText[2]]]
$endif
$endif
$if[$getTextSplitLength>2]
$if[$roleExists[$findRole[$splitText[3]]]==true]
$var[br;$var[br] $findRole[$splitText[3]]]
$var[br3;$findRole[$splitText[3]]]
$endif
$endif
$if[$and[$roleExists[$var[br1]]==false;$roleExists[$var[br2]]==false;$roleExists[$var[br3]]==false]==true]
$var[failed;true]
$var[failed_error;Invalid roles given in "Blacklisted Roles"! Try using role IDs separated by comma instead.]
$endif
$var[br;$replaceText[$var[br];  ;;-1]]
$var[br;$replaceText[$var[br];  ;;-1]]
$var[br;$replaceText[$var[br]; ;,;-1]]
$textSplit[$var[br];,]
$var[br_n;0]
$if[$roleExists[$splitText[1]]==true] $var[br_n;$sum[$var[br_n];1]] $endif
$if[$roleExists[$splitText[2]]==true] $var[br_n;$sum[$var[br_n];1]] $endif
$if[$roleExists[$splitText[3]]==true] $var[br_n;$sum[$var[br_n];1]] $endif
$var[br_length;$var[br_n]]
$if[$var[br_length]>1]
$var[br_msg;<@&$splitText[1]>
<@&$splitText[2]>]
$var[br_plural;s]
$else
$var[br_msg;<@&$splitText[1]>]
$endif
$if[$var[br_length]>2]
$var[br_msg;$var[br_msg]
<@&$splitText[3]>]
$endif
$if[$checkContains[$var[br_msg];<@&>]==true]
$var[failed;true]
$var[failed_error;Please use only one role value (ID, name, or mention) when specifying roles. Combining multiple values may cause errors. If you are using only one role, try using its ID. If the problem persists, contact a bot developer, this error comes from the "Blacklisted Roles" input.]
$endif
$endif
$if[$var[failed]==true]
$color[$var[error_color]]
$title[Failed!]
$description[Sorry **$username**, this action failed because of the following error:
```$var[failed_error]```]
$footer[If you think this is a bug report it to a Bot Developer!]
$ephemeral
$stop
$endif
$if[$var[sr_msg]==]
$var[sr_msg;``Not given!``]
$endif
$if[$var[br_msg]==]
$var[br_msg;``Not given!``]
$endif
$setServerVar[tickets3;$replaceText[$var[sr]-$var[br]; ;;-1]]
$color[$var[success_color]]
$title[Success!]
$description[The previous values have been successfully updated to the new values!]
$addField[Staff Role$var[sr_plural];$var[sr_msg];yes]
$addField[Blacklisted Role$var[br_plural];$var[br_msg];yes]
$ephemeral
$stop $c[s]
$endif
$if[$customID==tkt_cfg-$authorID]
$removeButtons
$if[$or[$var[is_staff]==false;$checkUserPerms[$authorID;manageserver]==false]==true]
$removeButtons
$title[$var[sf_title]]
$description[$var[sf_descr]]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$var[t_title;$input[ticket-title]]
$var[t_desc;$input[ticket-description]]
$var[t_footer;$input[ticket-footer]]
$var[t_color;$input[ticket-color]]
$var[t_image;$input[ticket-image]]
> *This is just a preview of the embed, you can dismiss it.*
$try
$footer[$var[t_footer]]
$var[embed_data;$var[t_footer]]
$endtry
$if[$isValidHex[$var[t_color]]==true]
$try
$color[$var[t_color]]
$catch
$color[$var[main_color]]
$var[t_color;$var[main_color]]
$endtry
$var[embed_data;$var[embed_data]≈$var[t_color]]
$else
$color[$var[main_color]]
$var[embed_data;$var[embed_data]≈]
$endif
$try
$title[$var[t_title]]
$var[embed_data;$var[embed_data]≈$var[t_title]]
$catch
$title[Ticket Menu]
$var[embed_data;$var[embed_data]≈]
$endtry
$try
$description[$var[t_desc]]
$var[embed_data;$var[embed_data]≈$var[t_desc]]
$catch
$description[Open a new Ticket using the interaction below this message!]
$var[embed_data;$var[embed_data]≈]
$endtry
$try
$image[$var[t_image]]
$var[embed_data;$var[embed_data]≈$var[t_image]]
$catch
$var[embed_data;$var[embed_data]≈]
$endtry
$setChannelVar[tickets2;$var[embed_data]]
$ephemeral
$endif
$c[here]
$if[$customID==tkt_pnlact_delete-$authorID]
$if[$input[panelid]==1]
$var[input;$input[panelid]]
$else
$var[input;$sum[$input[panelid];1]]
$endif
$if[$or[$var[is_staff]==false;$checkUserPerms[$authorID;manageserver]==false]==true]
$removeButtons
$title[$var[sf_title]]
$description[$var[sf_descr]]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$if[$isNumber[$var[input]]==false]
$removeButtons
$description[Invalid Panel ID given! It must be a valid ID from **1-$var[panel_limit]**, to know the IDs of all the existing panels just use the ticket menu "Setup Ticket Panel" button.]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$if[$or[$var[input]<1;$var[input]>$var[panel_limit]]==true]
$removeButtons
$description[Invalid Panel ID given! __It must be a valid ID from **1-$var[panel_limit]**__, you gave a numerical ID but it's not a valid one.]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$textSplit[$getChannelVar[tickets];≈]
$if[$var[input]==1]
$var[r;$splitText[2]]
$else
$var[r;$splitText[$var[input]]]
$endif
$if[$checkContains[$var[r];𝖑]==false]
$removeButtons
$description[Invalid Panel ID given! You gave a numerical ID but there are no panels linked to that ID.]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$try
$setChannelVar[tickets;$replaceText[$getChannelVar[tickets];≈$var[r];;1]]
$setChannelVar[tickets;$replaceText[$replaceText[$getChannelVar[tickets];$var[r];;1];≈≈;≈;-1]]
$catch
$description[Couldn't remove the panel with the given ID, please report this error to a Bot Developer.]
$color[$var[error_color]]
$ephemeral
$stop
$endtry
$if[$var[input]==1] $var[p;1] $else $var[p;$sub[$var[input];1]] $endif
$title[Success!]
$description[> You successfully **deleted** the panel ID **$var[p]**!]
$color[$var[success_color]]
$ephemeral
$stop $c[s]
$endif
$c[st]
$if[$customID==tkt_add_pnl-$authorID]
$if[$or[$var[is_staff]==false;$checkUserPerms[$authorID;manageserver]==false]==true]
$stop
$endif
$removeButtons
$textSplit[$getChannelVar[tickets];≈]
$var[l;$getTextSplitLength]
$var[n;1]
$if[$var[l]>1]
$eval[$repeatMessage[2;$repeatMessage[5;%{DOL}%optOff[
%{DOL}%textSplit[%{DOL}%getChannelVar[tickets\]\;≈\]
%{DOL}%var[s\;%{DOL}%splitText[%{DOL}%sum[%{DOL}%var[n\]\;1\]\]\]
%{DOL}%textSplit[%{DOL}%var[s\]\;𝖑\]
%{DOL}%var[%{DOL}%var[n\]_title\;%{DOL}%splitText[1\]\]
%{DOL}%var[%{DOL}%var[n\]_description\;%{DOL}%splitText[2\]\]
%{DOL}%if[%{DOL}%var[%{DOL}%var[n\]_description\]!=\]
%{DOL}%try %{DOL}%addField[ID #%{DOL}%var[n\] - %{DOL}%var[%{DOL}%var[n\]_title\]\;```%{DOL}%var[%{DOL}%var[n\]_description\]```\] %{DOL}%endtry
%{DOL}%endif
%{DOL}%var[n\;%{DOL}%sum[%{DOL}%var[n\]\;1\]\]
\]]]]
$endif
$title[Panels Management]
$description[> Manage your ticket panels using the buttons below this embed, leave everything as default if you want to use a button to open the ticket instead (no panels), you can setup a maximum of **$var[panel_limit]** panels.]
$color[$var[success_color]]
$footer[When you are done configuring the panels press the "Done" button to save changes.]
$if[$var[l]>$var[panel_limit]]
$addButton[no;tkt_pnlact_mdl_add-$authorID;Max $var[panel_limit] panels!;primary;yes;]
$else
$addButton[no;tkt_pnlact_mdl_add-$authorID;Add new panel;primary;no;]
$endif
$if[$var[l]>1]
$var[d;no]
$else
$var[d;yes]
$endif
$addButton[no;tkt_pnlact_mdl_edit-$authorID;Edit panel;secondary;$var[d];]
$addButton[no;tkt_pnlact_mdl_delete-$authorID;Delete panel;danger;$var[d];]
$addButton[no;tkt_pnlact_done-$authorID;Done;success;no;]
$ephemeral
$stop $c[s]
$endif
$if[$customID==tkt_pnlact_done-$authorID]
$removeButtons
$title[Success!]
$description[> Successfully saved changes! No errors detected.]
$color[$var[success_color]]
$try $var[d;$deleteIn[3s]] $endtry
$stop $c[s]
$endif

$if[$checkContains[$customID;tkt_pnlact_]==true]
$if[$checkContains[$customID;$authorID]==true]
$try $var[d;$deleteIn[5s]] $endtry
$endif
$endif
$if[$customID==tkt_open]
$removeButtons
$var[u;$getChannelVar[tickets;$channelID]]
$var[user;$var[u]]
$var[guild;$guildID]
$if[$or[$var[is_staff]==false;$checkUserPerms[$authorID;manageserver]==false]==true]
$removeButtons
$title[$var[sf_title]]
$description[$var[sf_descr]]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$try
$modifyChannelPerms[$channelID;+readmessages;+sendmessages;+embedlinks;+attachfiles;$var[u]]
$catch
$editChannelPerms[$channelID;$var[u];+sendmessages;+readmessages;+embedlinks;+attachfiles]
$endtry
$if[$checkContains[$channelName[$channelID];solved-]==false]
$title[Already Open!]
$description[Hey **$username**, this Ticket is already flagged as **open**! Are you trying to close it back?
You can use the Staff Panel to close this ticket back.]
$color[$var[error_color]]
$addButton[no;tkt_pnel;Staff Panel;primary;no;$var[panel_emoji]]
$ephemeral
$stop
$endif
$async[oa]
$useChannel[$channelID]
$sendEmbedMessage[$channelID;<@$var[u]>;Ticket Open!;;This Ticket has been opened by **$username[$authorID]#$discriminator[$authorID]**!
```Ticket Author Username: $username[$var[u]]#$discriminator[$var[u]]
Ticket Author's ID: $var[u]
Ticket unarchived by $username[$authorID]#$discriminator[$authorID]```;$var[success_color];$serverName[$guildID];$serverIcon[$guildID];;;;;;no]
$optOff[$modifyChannel[$channelID;$replaceText[$channelName[$channelID];solved-;;-1]]]
$endasync
$removeButtons
$title[Ticket opened back!]
$description[> ☑️ This Ticket is now **Open**! Read & Send Messages permissions has been granted back to <@$var[u]>, the Ticket's author. ]
$color[$var[success_color]]
$ephemeral
$stop $c[s]
$endif

$if[$customID==tkt_closecancel]
$removeButtons
$try
$setUserVar[tickets;$replaceText[$getUserVar[tickets];-$channelIDClose;;-1];$authorID]
$catch
$setUserVar[tickets;;$authorID]
$endtry
$description[> ☑️ Successfully cancelled this action! This Ticket **won't** get closed, if you want to close it you can use the **Close Ticket** button again.]
$color[$var[success_color]]
$stop $c[s]
$endif

$if[$customID==tkt_pnlact_edit-$authorID]
$if[$input[panelid]==1]
$var[input;$input[panelid]]
$else
$var[input;$sum[$input[panelid];1]]
$endif
$var[newtitle;$input[paneltitle]]
$var[newdesc;$input[paneldescription]]
$if[$isNumber[$var[input]]==false]
$removeButtons
$description[Invalid Panel ID given! It must be a valid ID from **1-$var[panel_limit]**, to know the IDs of all the existing panels just use the ticket menu "Setup Ticket Panel" button.]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$if[$var[input]!=8]
$if[$or[$var[input]<1;$var[input]>$var[panel_limit]]==true]
$removeButtons
$description[Invalid Panel ID given! __It must be a valid ID from **1-$var[panel_limit]**__, you gave a numerical ID but it's not a valid one.]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$endif
$textSplit[$getChannelVar[tickets];≈]
$if[$var[input]==1]
$var[r;$splitText[2]]
$else
$var[r;$splitText[$var[input]]]
$endif
$if[$checkContains[$var[r];𝖑]==false]
$removeButtons
$description[Invalid Panel ID given! You gave a numerical ID but there are no panels linked to that ID.]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$textSplit[$var[r];𝖑]
$if[$var[newtitle]==]
$var[newtitle;$splitText[1]]
$var[title_extra; — Nothing changed!]
$endif
$if[$var[newdesc]==]
$var[newdesc;$splitText[2]]
$var[desc_extra; — Nothing changed!]
$endif
$try
$setChannelVar[tickets;$replaceText[$getChannelVar[tickets];$var[r];$var[newtitle]𝖑$var[newdesc];1]]
$catch
$try
$setChannelVar[tickets;$replaceText[$getChannelVar[tickets];$var[r];$var[newtitle]𝖑$cropText[$var[newdesc];30;];1]]
$catch
$try
$setChannelVar[tickets;$replaceText[$getChannelVar[tickets];$var[r];$var[newtitle]𝖑$cropText[$var[newdesc];20;];1]]
$catch
$title[Unexpected Error!]
$description[Sorry, there has been an issue while trying to edit this panel, all the values you gave were right, the error is from our side!]
$addField[Error Message;```Exceeded variable value while changing Ticket Panel title/description (Value is "$charCount[$getChannelVar[tickets]]")```;yes]
$footer[Please report this to the Bot Developer, if this isn't fixed just open a new ticket menu setup.]
$color[$var[error_color]]
$endtry
$endtry
$endtry
$title[Success!]
$description[> Successfully edited the panel ID **$var[input]**!]
$if[$var[input]==1]
$addField[ID;```$var[input]```;yes]
$else
$addField[ID;```$sub[$var[input];1]```;yes]
$endif
$addField[New Title$var[title_extra];```$var[newtitle]```;yes]
$addField[New Description$var[desc_extra];```$var[newdesc]```;yes]
$color[$var[success_color]]
$ephemeral
$stop $c[s]
$endif
$if[$customID==tkt_pnlact_add-$authorID]
$if[$or[$var[is_staff]==false;$checkUserPerms[$authorID;manageserver]==false]==true]
$removeButtons
$title[$var[sf_title]]
$description[$var[sf_descr]]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$textSplit[$getChannelVar[tickets];≈]
$var[l;$getTextSplitLength]
$if[$var[l]>$var[panel_limit]]
$description[You cannot create another Ticket Panel, there's a limit of **$var[panel_limit]** panels! You can either remove a panel or create another ticket menu.]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$title[Success!]
$description[Successfully added panel ID **$var[l]**!]
$addField[Panel ID;```$var[l]```;yes]
$addField[Panel Title;```$input[paneltitle]```;yes]
$addField[Panel Description;```$input[paneldescription]```;yes]
$color[$var[success_color]]
$try
$setChannelVar[tickets;$getChannelVar[tickets]≈$input[paneltitle]𝖑$input[paneldescription]]
$catch
$try
$setChannelVar[tickets;$getChannelVar[tickets]≈$input[paneltitle]𝖑$cropText[$input[paneldescription];30]~]
$catch
$setChannelVar[tickets;≈$input[paneltitle]𝖑$input[paneldescription]]
$endtry
$endtry
$ephemeral
$stop $c[s]
$endif $c[e]
$if[$customID==tkt_pnl_send-$authorID]
$if[$or[$var[is_staff]==false;$checkUserPerms[$authorID;manageserver]==false]==true]
$stop
$endif
$removeButtons
$textSplit[$getChannelVar[tickets2];≈]
$var[t_footer;$splitText[1]]
$var[t_color;$splitText[2]]
$var[t_title;$splitText[3]]
$var[t_desc;$splitText[4]]
$var[t_image;$splitText[5]]
$textSplit[$getChannelVar[tickets];≈]
$var[l;$getTextSplitLength]
$var[n;1]
$if[$var[l]>1]
$var[type;selection menu]
$newSelectMenu[tmenu-open;1;1;Select a Ticket panel!]
$eval[$repeatMessage[2;$repeatMessage[5;%{DOL}%optOff[
%{DOL}%textSplit[%{DOL}%getChannelVar[tickets\]\;≈\]
%{DOL}%var[s\;%{DOL}%splitText[%{DOL}%sum[%{DOL}%var[n\]\;1\]\]\]
%{DOL}%textSplit[%{DOL}%var[s\]\;𝖑\]
%{DOL}%var[%{DOL}%var[n\]_title\;%{DOL}%splitText[1\]\]
%{DOL}%var[%{DOL}%var[n\]_description\;%{DOL}%splitText[2\]\]
%{DOL}%if[%{DOL}%var[%{DOL}%var[n\]_description\]!=\]
%{DOL}%try
%{DOL}%addSelectMenuOption[tmenu-open\;%{DOL}%var[%{DOL}%var[n\]_title\]\;tkt_mdl_o-%{DOL}%replaceText[%{DOL}%var[%{DOL}%var[n\]_title\]-%{DOL}%var[n\]\;-\;~\;-1\]\;%{DOL}%var[%{DOL}%var[n\]_description\]\] 
%{DOL}%endtry
%{DOL}%endif
%{DOL}%var[n\;%{DOL}%sum[%{DOL}%var[n\]\;1\]\]
\]]]]
$else
$var[type;button]
$addButton[no;tkt_mdl_op-0;Open a Ticket;primary;no;$var[openticket_emoji]]
$endif
$if[$var[t_title]!=]
$title[$var[t_title]]
$else
$title[Ticket Menu]
$endif
$if[$var[t_desc]!=]
$description[$var[t_desc]]
$else
$description[Open a new Ticket using the $var[type] below this message!]
$endif
$if[$isValidHex[$var[t_color]]==true]
$color[$var[t_color]]
$else
$color[$var[main_color]]
$endif
$if[$var[t_footer]!=]
$footer[$var[t_footer]]
$endif
$if[$var[t_image]!=]
$try
$image[$var[t_image]]
$catch
$try
$image[$var[default_image]]
$endtry
$endtry
$else
$try
$image[$var[default_image]]
$endtry
$endif
$stop $c[s]
$endif
$if[$customID==tkt_pnel]
$removeButtons
$if[$var[is_staff]==false]
$removeButtons
$title[$var[sf_title]]
$description[$var[sf_descr]]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$removeComponent[$customID]
$var[u;$getChannelVar[tickets;$channelID]]
$var[user;$var[u]]
$title[Staff Panel]
$description[Hey **$username**, this is your staff panel! You can manage this ticket using the buttons below this message.]
$color[$var[main_color]]
$if[$checkContains[$getChannelVar[tickets2];%sticky%]==true]
$addButton[no;tkt_sticky;Mark as non-Sticky;success;no;$var[sticky_emoji]]
$endif
$if[$checkContains[$channelName[$channelID];solved-]==true]
$addButton[no;tkt_open;Open Ticket;success;no;$var[open_emoji]]
$else
$if[$checkContains[$getChannelVar[tickets2];%sticky%]==true]
$if[$var[hide_on_sticky]!=true]
$addButton[no;tkt_slvd--$authorID;Close & Save;primary;yes;$var[solved_emoji]]
$endif
$else
$addButton[no;tkt_slvd--$authorID;Close & Save;primary;no;$var[solved_emoji]]
$endif
$endif
$if[$checkContains[$getChannelVar[tickets2];%sticky%]==true]
$if[$var[hide_on_sticky]!=true]
$addButton[no;tkt_close;Close Ticket;danger;yes;$var[close_emoji]]
$endif
$else
$addButton[no;tkt_close;Close Ticket;danger;no;$var[close_emoji]]
$endif
$if[$getChannelVar[tickets3]!=]
$if[$userExists[$getChannelVar[tickets3]]==true]
$var[claimed_by;$getChannelVar[tickets3]]
$endif
$endif
$if[$var[claimed_by]==]
$addButton[no;tkt_claim;Claim Ticket;secondary;no;$var[claim_emoji]]
$else
$if[$or[$var[claimed_by]==$authorID;$isAdmin[$authorID]==true]==true]
$addButton[no;tkt_claim;Unclaim Ticket;secondary;no;$var[claim_emoji]]
$else
$addButton[no;tkt_claim;Claimed by $cropText[$username[$authorID];6;~];secondary;yes;$var[claim_emoji]]
$endif
$endif
$if[$checkContains[$getChannelVar[tickets2];%sticky%]==false]
$addButton[no;tkt_sticky;Mark as Sticky;secondary;no;$var[sticky_emoji]]
$endif
$if[$var[hide_on_sticky]==true]
$if[$checkContains[$getChannelVar[tickets2];%sticky%]==true]
$var[berk_4ever;no]
$else
$var[berk_4ever;yes]
$endif
$else
$var[berk_4ever;yes]
$endif
$addButton[$var[berk_4ever];tkt_usr;User Info;secondary;no;$var[info_emoji]]
$ephemeral
$stop $c[s]
$endif
$if[$customID==tkt_claim]
$removeButtons
$if[$var[is_staff]==false]
$removeButtons
$title[$var[sf_title]]
$description[$var[sf_descr]]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$var[u;$getChannelVar[tickets;$channelID]]
$var[user;$var[u]]
$var[claimed_msg;| Claimed by $username[$authorID]#$discriminator[$authorID]]
$var[format;$channelID $authorID $channelID]
$var[format;$replaceText[$var[format]; ;;-1]]
$addButton[no;tkt_pnel;Staff Panel;primary;no;$var[panel_emoji]]
$if[$getChannelVar[tickets3]!=]
$if[$userExists[$getChannelVar[tickets3]]==true]
$var[claimed_by;$getChannelVar[tickets3]]
$endif
$endif
$if[$var[claimed_by]==]
$async[logs_block]
$if[$serverChannelExists[$var[logs]]]
$try
$sendEmbedMessage[$var[logs];;Ticked Claimed;;Ticket ``#$channelName[$channelID]`` (<#$channelID>) by <@$var[u]> (**$username[$var[u]]#$discriminator[$var[u]]**) has been __claimed__ by the staff member <@$authorID> (**$username[$authorID]#$discriminator[$authorID]**)!
;$var[success_color];;;;;;;;no]
$endtry
$endif
$endasync
$sendEmbedMessage[$channelID;;Ticked Claimed;;Hey **$username[$var[u]]**, this ticket has been claimed by <@$authorID> (**$username[$authorID]#$discriminator[$authorID]**)!
;$var[main_color];;;;;;;;no]
$setChannelVar[tickets3;$authorID]
$title[Successfully claimed!]
$description[> ☑️ **$username[$authorID]** You successfully claimed this ticket!]
$color[$var[success_color]]
$textSplit[$getServerVar[tickets3];-]
$var[ts1;$splitText[1]]
$var[ts2;$splitText[2]]
$textSplit[$var[ts1];,]
$try $editChannelPerms[$channelID;$authorID;+sendmessages;+readmessages;+embedlinks;+attachfiles] $endtry
$if[$roleExists[$splitText[1]]==true] $try $editChannelPerms[$channelID;$splitText[1];-sendmessages;+readmessages;+embedlinks;+attachfiles] $endtry $endif
$if[$roleExists[$splitText[2]]==true] $try $editChannelPerms[$channelID;$splitText[2];-sendmessages;+readmessages;+embedlinks;+attachfiles] $endtry $endif
$if[$roleExists[$splitText[3]]==true] $try $editChannelPerms[$channelID;$splitText[3];-sendmessages;+readmessages;+embedlinks;+attachfiles] $endtry $endif
$try
$optOff[$modifyChannel[$channelID;!unchanged;$channelTopic $var[claimed_msg] ($authorID)]]
$endtry
$else
$if[$isAdmin[$authorID]==false]
$if[$authorID!=$var[claimed_by]]
$removeButtons
$description[Hey **$username**, you can't claim this ticket! This ticket has been claimed by <@$var[claimed_by]>, they or an administrator must unclaim it.]
$color[$var[error_color]]
$stop
$endif
$endif
$async[logs_block]
$if[$serverChannelExists[$var[logs]]]
$try
$sendEmbedMessage[$var[logs];;Ticked Unclaimed;;Ticket ``#$channelName[$channelID]`` (<#$channelID>) by <@$var[u]> (**$username[$var[u]]#$discriminator[$var[u]]**) has been __unclaimed__ by the staff member <@$authorID> (**$username[$authorID]#$discriminator[$authorID]**)!
;$var[neutral_color];;;;;;;;no]
$endtry
$endif
$endasync
$sendEmbedMessage[$channelID;;Ticked Unclaimed;;Hey **$username[$var[u]]**, this ticket has been __unclaimed__ by <@$authorID> (**$username[$authorID]#$discriminator[$authorID]**)!
;$var[main_color];;;;;;;;no]
$setChannelVar[tickets3;]
$title[Successfully unclaimed!]
$description[> ☑️ **$username[$authorID]** You successfully marked this ticket as **unclaimed**!]
$color[$var[success_color]]
$textSplit[$getServerVar[tickets3];-]
$var[ts1;$splitText[1]]
$var[ts2;$splitText[2]]
$textSplit[$var[ts1];,]
$try $editChannelPerms[$channelID;$authorID;/sendmessages;/readmessages;+embedlinks;+attachfiles] $endtry
$if[$roleExists[$splitText[1]]==true] $try $editChannelPerms[$channelID;$splitText[1];+sendmessages;+readmessages;+embedlinks;+attachfiles] $endtry $endif
$if[$roleExists[$splitText[2]]==true] $try $editChannelPerms[$channelID;$splitText[2];+sendmessages;+readmessages;+embedlinks;+attachfiles] $endtry $endif
$if[$roleExists[$splitText[3]]==true] $try $editChannelPerms[$channelID;$splitText[3];+sendmessages;+readmessages;+embedlinks;+attachfiles] $endtry $endif
$try
$async[topic_change]
$replyIn[10s]
$var[new_topic;$replaceText[$replaceText[$channelTopic;$var[claimed_msg];;-1];($authorID);;-1]]
$optOff[$modifyChannel[$channelID;!unchanged;$var[new_topic]]]
$endasync
$endtry
$endif
$stop $c[s]
$endif
$if[$customID==tkt_sticky]
$removeButtons
$if[$var[is_staff]==false]
$removeButtons
$title[$var[sf_title]]
$description[$var[sf_descr]]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$addButton[no;tkt_pnel;Staff Panel;primary;no;$var[panel_emoji]]
$if[$checkContains[$getChannelVar[tickets2];%sticky%]==true]
$setChannelVar[tickets2;$replaceText[$getChannelVar[tickets2];%sticky%;;-1]]
$title[Successfully Unmarked]
$description[Ticket successfully **unmarked** as sticky! Ticket's author and Staff is now able to close this ticket.]
$color[$var[success_color]]
$async[logs_block]
$if[$serverChannelExists[$var[logs]]]
$try
$sendEmbedMessage[$var[logs];;Ticked Unmarked as Sticky;;Ticket ``#$channelName[$channelID]`` (<#$channelID>) has been **unmarked as sticky** by <@$authorID> (**$username[$authorID]#$discriminator[$authorID]**)!
;$var[neutral_color];;;;;;;;no]
$endtry
$endif
$endasync
$else
$setChannelVar[tickets2;$getChannelVar[tickets2] %sticky%]
$title[Successfully Marked]
$description[Ticket successfully **marked** as sticky! Ticket's author and Staff is not able to close this ticket anymore till it gets unmarked as sticky.]
$color[$var[success_color]]
$async[logs_block]
$if[$serverChannelExists[$var[logs]]]
$try
$sendEmbedMessage[$var[logs];;Ticked Marked as Sticky;;Ticket ``#$channelName[$channelID]`` (<#$channelID>) has been **marked as sticky** by <@$authorID> (**$username[$authorID]#$discriminator[$authorID]**)!
;$var[success_color];;;;;;;;no]
$endtry
$endif
$endasync
$endif
$stop $c[s]
$endif
    $c[ ... Thanks Xloxn#4050 for the "Acknowledgements" and "Key permissions" fields. ]
$if[$checkContains[$customID;tkt_usr]==true]
$removeButtons
$textSplit[$customID;-]
$if[$splitText[2]!=]
$var[u;$splitText[2]]
$var[type;logs]
$else
$var[u;$getChannelVar[tickets;$channelID]]
$endif
$var[user;$var[u]]
$if[$userExists[$var[u]]==false]
$title[Ticket Panel (Failed!)]
$description[> Couldn't retrieve the user information about this ticket's author!]
$color[$var[error_color]]
$if[$var[type]==logs]
$ephemeral
$endif
$stop
$endif
$var[keyperms;$trimSpace[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$replaceText[$toTitleCase[$replaceText[$toLowercase[$userPerms[$var[u];-1;, ], ];_; ;-1]];Use External Emojis, ;;-1];Use External Stickers, ;;-1];Connect ,;;-1];Request To Speak, ;;-1];Use Vad, ;;-1];Use Application Commands, ;;-1];Create Public Threads, ;;-1];Send Messages In Threads, ;;-1];Manage Emojis And Stickers, ;;-1];Connect, ;;-1];Speak, ;;-1];Move Members, ;;-1];Read Message History, ;;-1];Create Instant Invite, ;;-1];Send Tts Messages, ;;-1];Embed Links, ;;-1];View Guild Insights, ;;-1];Manage Events, ;;-1];Priority Speaker, ;;-1];Stream, ;;-1];Add Reactions, ;;-1];Mute Members, ;;-1];Deafen Members, ;;-1];Manage Threads, ;;-1];View Audit Log, ;;-1];Attach Files, ;;-1];Manage Guild, ;;-1];Create Private Threads, ;;-1];Change Nickname, ;;-1];Manage Webhooks, ;;-1]]]
$var[keyperms;$trimSpace[$var[keyperms]]]
$var[keyperms;$cropText[$var[keyperms];$sub[$charCount[$var[keyperms]];1];]]
$if[$serverOwner==$var[u]]
$var[Acknowledgements;Server Owner]
$elseif[$checkUserPerms[$var[u];manageserver]==true]
$var[Acknowledgements;Server Admin]
$elseif[$checkUserPerms[$var[u];admin]==true]
$var[Acknowledgements;Administrator]
$elseif[$or[$checkUserPerms[$var[u];kick]==true;$checkUserPerms[$var[u];ban]==true;$checkUserPerms[$var[user];managemessages]==true;$checkUserPerms[$var[u];moderatemembers]==true]==true]
$var[Acknowledgements;Moderator]
$elseif[$and[$checkUserPerms[$var[user];admin;ban;kick]==false;$checkUserPerms[$var[u];sendmessages]==true]==true]
$var[Acknowledgements;Normal Member]
$elseif[$checkUserPerms[$var[u];sendmessages]==false]
$var[Acknowledgements;Normal Member]
$else
$var[Acknowledgements;Normal Member]
$endif
$if[$var[Acknowledgements]==]
$var[Acknowledgements;Unknown, couldn't find!]
$endif
$if[$var[keyperms]==]
$var[keyperms;Couldn't find!]
$endif
$title[Ticket Button - User Info]
$author[$username[$var[u]]#$discriminator[$var[u]]'s user info]
$authorIcon[$userAvatar[$var[u]]]
$description[> :identification_card: Information about the Ticket's author.]
$addField[Identificators;``$var[u]`` <@$var[u]>;no]
$addField[Joined;```$userJoined[$var[u];Mon, Jan 2, 2006 3:04 PM]```;yes]
$addField[Registered;```$userJoinedDiscord[$var[u];Mon, Jan 2, 2006 3:04 PM]```;yes]
$addField[Key Permissions;```$var[keyperms]```;no]
$addField[Acknowledgements;
```$var[Acknowledgements]```
;no]
$thumbnail[$userAvatar[$var[u]]]
$if[$var[type]!=logs]
$addButton[no;tkt_pnel;Back to the Panel;primary;no;$var[back_to_panel_emoji]]
$endif
$addButton[no;tkt_avtr-$var[u];User Avatar;secondary;no;]
$color[$var[main_color]]
$if[$var[type]==logs]
$ephemeral
$endif
$stop $c[s]
$endif
$if[$checkContains[$customID;tkt_avtr-]==true]
$removeButtons
$textSplit[$customID;-]
$var[u;$splitText[2]]
$var[user;$var[u]]
$var[cut;$replaceText[$replaceText[$replaceText[$replaceText[$userAvatar[$var[u]];gif;;1];png;;1];jpg;;1];webp;;1]]
$var[av;$userAvatar[$var[u]]]
$title[Ticket Button - User Info - Avatar]
$author[$username[$var[u]]#$discriminator[$var[u]]'s avatar!]
$authorIcon[$userAvatar[$var[u]]]
$image[$var[av]?size=2048]
$if[$checkContains[$var[av];gif]==true]
$addButton[no;$var[av]?size=2048;GIF;link;no;]
$endif
$addButton[no;$var[cut]png?size=2048;PNG;link;no;]
$addButton[no;$var[cut]jpg?size=2048;JPG;link;no;]
$addButton[no;$var[cut]webp?size=2048;WEBP;link;no;]
$color[$var[main_color]]
$ephemeral
$stop $c[s]
$endif
$if[$customID==tkt_close]
$removeButtons
$if[$checkContains[$getChannelVar[tickets2];%sticky%]==true]
$title[You can't close this Ticket!]
$description[Hey **$username**, this Ticket is marked as **Sticky**! It can't be closed till a staff member unmarks it using the Ticket Panel.]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$var[u;$getChannelVar[tickets;$channelID]]
$var[user;$var[u]]
$title[Closing Ticket!]
$description[Hey <@$authorID>, this ticket is closing <t:$sum[$getTimestamp;$var[close_in]]:R>!]
$color[$var[error_color]]
$addButton[no;tkt_closenow;Close Now;danger;no;$var[close_emoji]]
$addButton[no;tkt_closecancel;Cancel;primary;no;]
$try
$setUserVar[tickets;$getUserVar[tickets]-$channelIDClose;$authorID]
$catch
$setUserVar[tickets;$channelIDClose;$authorID]
$endtry
$var[ch;$channelID]
$var[guild;$guildID]
$async[close_ticket]
$replyIn[$var[close_in]s]
$if[$channelExists[$channelID]==false]
$stop
$endif
$if[$checkContains[$getUserVar[tickets;$authorID];$var[ch]Close]==true]
$try
$if[$checkContains[$channelName[$channelID];solved-]==false]
$try
$var[dm_id;$sendEmbedMessage[$dmChannelID[$var[u]];;Ticket Closed;$getBotInvite;Hey **$username[$var[u]]**, your ticket ``#$channelName[$channelID]`` has been closed by <@$authorID> (**$username[$authorID]#$discriminator[$authorID]**)!

$replaceText[$var[rt_msg];{server};$serverName[$guildID];-1];$var[main_color];$serverName[$guildID];$serverIcon[$guildID];$var[rt_footer];;;;;yes]]
$useChannel[$dmChannelID[$var[u]]]
$if[$var[rating]==true]
$addButton[no;tkt_rtng-verybad-$var[guild];Very bad!;danger;no;;$var[dm_id]]
$addButton[no;tkt_rtng-bad-$var[guild];Bad!;danger;no;;$var[dm_id]]
$addButton[no;tkt_rtng-regular-$var[guild];Regular;primary;no;;$var[dm_id]]
$addButton[no;tkt_rtng-good-$var[guild];Good!;success;no;;$var[dm_id]]
$addButton[no;tkt_rtng-verygood-$var[guild];Very good!;success;no;;$var[dm_id]]
$else
$try
$addButton[no;$getBotInvite;Invite $username[$botID]!;link;no;;$var[dm_id]]
$catch
$addButton[no;$getBotInvite;Invite me!;link;no;;$var[dm_id]]
$endtry
$endif
$endtry
$endif
$setUserVar[tickets2;;$var[u]]
$if[$serverChannelExists[$var[logs]]==true]
$try
$var[logs_id;$sendEmbedMessage[$var[logs];;;;
> Ticket ``#$channelName[$var[ch]]`` has been closed <t:$getTimestamp:R>! (<t:$getTimestamp:F>)

**Ticket's Author**
```$username[$var[u]]#$discriminator[$var[u]] ($var[u])```**Closed By**
```$username[$authorID]#$discriminator[$authorID] ($authorID)```**Ticket ID**
```$var[ch]```
;$var[error_color]
;Logs - Ticket Closed!
;
;;;;;yes;yes]]
$endtry
$try
$async[logs_btns]
$useChannel[$var[logs]]
$addButton[no;tkt_usr-$authorID;Ticket Author's info;secondary;no;$var[info_emoji];$var[logs_id]]
$endasync
$endtry
$endif
$deleteChannels[$var[ch]]
$catch
$channelSendMessage[$var[ch];Hey <@$authorID>, there's been an error trying to close this ticket, I couldn't delete the ticket channel, please make sure I have the `manage channels` permission.]
$endtry
$endif
$endasync
$ephemeral
$stop $c[s]
$endif
$c[ here close cancel ]
$if[$customID==tkt_closenow]
$var[u;$getChannelVar[tickets;$channelID]]
$var[user;$var[u]]
$var[guild;$guildID]
$if[$checkContains[$getChannelVar[tickets2];%sticky%]==true]
$title[You can't close this Ticket!]
$description[Hey **$username**, this Ticket is marked as **Sticky**! It can't be closed till a staff member unmarks it using the Ticket Panel.]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$if[$checkContains[$channelName[$channelID];solved-]==false]
$try
$var[dm_id;$sendEmbedMessage[$dmChannelID[$var[u]];;Ticket Closed;$getBotInvite;Hey **$username[$var[u]]**, your ticket ``#$channelName[$channelID]`` has been closed by <@$authorID> (**$username[$authorID]#$discriminator[$authorID]**)!

$replaceText[$var[rt_msg];{server};$serverName[$guildID];-1];$var[main_color];$serverName[$guildID];$serverIcon[$guildID];$var[rt_footer];;;;;yes]]
$useChannel[$dmChannelID[$var[u]]]
$if[$var[rating]==true]
$addButton[no;tkt_rtng-verybad-$var[guild];Very bad!;danger;no;;$var[dm_id]]
$addButton[no;tkt_rtng-bad-$var[guild];Bad!;danger;no;;$var[dm_id]]
$addButton[no;tkt_rtng-regular-$var[guild];Regular;primary;no;;$var[dm_id]]
$addButton[no;tkt_rtng-good-$var[guild];Good!;success;no;;$var[dm_id]]
$addButton[no;tkt_rtng-verygood-$var[guild];Very good!;success;no;;$var[dm_id]]
$else
$try
$addButton[no;$getBotInvite;Invite $username[$botID]!;link;no;;$var[dm_id]]
$catch
$addButton[no;$getBotInvite;Invite me!;link;no;;$var[dm_id]]
$endtry
$endif
$endtry
$endif
$if[$serverChannelExists[$var[logs]]==true]
$try
$var[ch;$channelID]
$var[logs_id;$sendEmbedMessage[$var[logs];;;;
> Ticket ``#$channelName[$var[ch]]`` has been closed <t:$getTimestamp:R>! (<t:$getTimestamp:F>)

**Ticket's Author**
```$username[$var[u]]#$discriminator[$var[u]] ($var[u])```**Closed By**
```$username[$authorID]#$discriminator[$authorID] ($authorID)```**Ticket ID**
```$var[ch]```
;$var[error_color]
;Logs - Ticket Closed!
;
;;;;;yes;yes]]
$endtry
$try
$async[logs_btns]
$useChannel[$var[logs]]
$addButton[no;tkt_usr-$authorID;Ticket Author's info;secondary;no;$var[info_emoji];$var[logs_id]]
$endasync
$endtry
$endif
$deleteChannels[$channelID]
$setUserVar[tickets2;;$var[u]]
$stop $c[s]
$endif
$if[$checkContains[$customID;tkt_slvd]==true]
$removeButtons
$if[$or[$var[is_staff]==false;$checkUserPerms[$authorID;manageserver]==false]==true]
$removeButtons
$title[$var[sf_title]]
$description[$var[sf_descr]]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$var[u;$getChannelVar[tickets;$channelID]]
$var[user;$var[u]]
$var[guild;$guildID]
$if[$checkContains[$getChannelVar[tickets2];%sticky%]==true]
$title[You can't close this Ticket!]
$description[Hey **$username**, this Ticket is marked as **Sticky**! It can't be closed till a staff member unmarks it using the Ticket Panel.]
$color[$var[error_color]]
$ephemeral
$stop
$endif
$if[$checkContains[$channelName[$channelID];solved-]==true]
$title[Already Closed & Solved!]
$description[Hey **$username**, this Ticket is already flagged as Closed & Solved! Are you trying to open it back?
You can use the Staff Panel to open this ticket back.]
$color[$var[error_color]]
$addButton[no;tkt_pnel;Staff Panel;primary;no;$var[panel_emoji]]
$ephemeral
$stop
$endif
$try
$var[dm_id;$sendEmbedMessage[$dmChannelID[$var[u]];;Ticket Closed;$getBotInvite;Hey **$username[$var[u]]**, your ticket ``#$channelName[$channelID]`` has been closed by <@$authorID> (**$username[$authorID]#$discriminator[$authorID]**)!

$replaceText[$var[rt_msg];{server};$serverName[$guildID];-1];$var[main_color];$serverName[$guildID];$serverIcon[$guildID];$var[rt_footer];;;;;yes]]
$useChannel[$dmChannelID[$var[u]]]
$if[$var[rating]==true]
$addButton[no;tkt_rtng-verybad-$var[guild];Very bad!;danger;no;;$var[dm_id]]
$addButton[no;tkt_rtng-bad-$var[guild];Bad!;danger;no;;$var[dm_id]]
$addButton[no;tkt_rtng-regular-$var[guild];Regular;primary;no;;$var[dm_id]]
$addButton[no;tkt_rtng-good-$var[guild];Good!;success;no;;$var[dm_id]]
$addButton[no;tkt_rtng-verygood-$var[guild];Very good!;success;no;;$var[dm_id]]
$else
$try
$addButton[no;$getBotInvite;Invite $username[$botID]!;link;no;;$var[dm_id]]
$catch
$addButton[no;$getBotInvite;Invite me!;link;no;;$var[dm_id]]
$endtry
$endif
$endtry
$async[bl]
$useChannel[$channelID]
$var[saved_id;$sendEmbedMessage[$channelID;;Closed & Saved;;This Ticket has been Closed & Saved by **$username[$authorID]#$discriminator[$authorID]**!
```This Ticket won't be seen by the person that opened it anymore, only staffs, if you wish to open this ticket back just use the panel!```;$var[main_color];$serverName[$guildID];$serverIcon[$guildID];;;;;;yes]]

$addButton[no;tkt_close;Close Ticket;danger;no;$var[close_emoji];$var[saved_id]]
$addButton[no;tkt_pnel;Staff Panel;primary;no;$var[panel_emoji];$var[saved_id]]
$endasync
$optOff[$modifyChannel[$channelID;solved-$channelName[$channelID]]]
$editChannelPerms[$channelID;$var[u];-sendmessages;-readmessages]
$removeButtons
$title[Closed & Saved]
$description[> ☑️ Successfully **Closed & Saved** this ticket! You still can use the panel to perform other actions such as actually closing this ticket. ]
$color[$var[success_color]]
$ephemeral
$stop $c[s]
$endif
$if[$checkContains[$customID;tkt_rtng-]==true]
$defer
$if[$varExists[tickets2]==false]
$removeButtons
$try
$if[$userExists[$botOwnerID]==true]
$var[bot_dev;**$username[$botOwnerID]#$discriminator[$botOwnerID]** (The Bot Developer)]
$else
$var[bot_dev;the Bot Developer]
$endif
$catch
$var[bot_dev;the Bot Developer]
$endtry
$title[Error!]
$description[Thanks for rating, your rating **wasn't** sent anywhere since there has been an **error** trying to set your anonymous rate, please contact $var[bot_dev], and send them the following error message.
```error: Missing variable "tickets2", this variable must be added in order to make the rating system work.```]
$color[$var[error_color]]
$stop
$endif
$textSplit[$customID;-]
$var[rate;$splitText[2]]
$var[guild;$splitText[3]]
$removeButtons
$if[$checkContains[$getServerVar[tickets2;$var[guild]];--]==false]
$setServerVar[tickets2;0--0--0--0--0;$var[guild]]
$endif
$textSplit[$getServerVar[tickets2;$var[guild]];--]
$if[$var[rate]==verybad]
$setServerVar[tickets2;$sum[0$splitText[1];1]--$splitText[2]--$splitText[3]--$splitText[4]--$splitText[5];$var[guild]]
$var[feedback_msg;$var[negative_rate]]
$endif
$if[$var[rate]==bad]
$setServerVar[tickets2;$splitText[1]--$sum[0$splitText[2];1]--$splitText[3]--$splitText[4]--$splitText[5];$var[guild]]
$var[feedback_msg;$var[negative_rate]]
$endif
$if[$var[rate]==regular]
$setServerVar[tickets2;$splitText[1]--$splitText[2]--$sum[0$splitText[3];1]--$splitText[4]--$splitText[5];$var[guild]]
$var[feedback_msg;$var[positive_rate]]
$endif
$if[$var[rate]==good]
$setServerVar[tickets2;$splitText[1]--$splitText[2]--$splitText[3]--$sum[0$splitText[4];1]--$splitText[5];$var[guild]]
$var[feedback_msg;$var[positive_rate]]
$endif
$if[$var[rate]==verygood]
$setServerVar[tickets2;$splitText[1]--$splitText[2]--$splitText[3]--$splitText[4]--$sum[0$splitText[5];1];$var[guild]]
$var[feedback_msg;$var[positive_rate]]
$endif
$title[Thank you!]
$description[$replaceText[$var[feedback_msg];{server};$serverName[$var[guild]];-1]]
$footer[$username[$botID]'s Ticket System]
$color[$var[neutral_color]]
$try
$addButton[no;$getBotInvite;Invite $username[$botID]!;link;no;]
$catch
$addButton[no;$getBotInvite;Invite me!;link;no;]
$endtry
$stop $c[s]
$endif
$suppressErrors
$c[Code by kem.rl]



Code 4 :
Langue : BDScript 2
Trigger : $onInteraction

$nomention
$if[$checkContains[$message;tkt_mdl_o-]==true]
$optOff[
$var[index;$replaceText[$message;tkt_mdl_o-;;1]]
$newModal[tkt_actop-$replaceText[$var[index];-;~;-1];Quel est votre problème ?]
$addTextInput[subject;paragraph;Sujet de votre Ticket;1;200;no;;Ici écrivez le sujet de votre ticket, vous pouvez le laissez vide aussi.]
]
$endif
$if[$checkContains[$customID;tkt_mdl_op-]==true]
$optOff[
$var[index;$replaceText[$customID;tkt_mdl_op-;1;-1]]
$newModal[tkt_actop-$replaceText[$var[index];-;~;-1];Quel est votre problème ?]
$addTextInput[subject;paragraph;Sujet de votre Ticket;1;200;no;;Ici écrivez le sujet de votre ticket, vous pouvez le laissez vide aussi.]
]
$endif
$if[$customID==tkt_pnlact_mdl_delete-$authorID]
$newModal[tkt_pnlact_delete-$authorID;Delete an existing panel]
$addTextInput[panelid;short;Panel ID;1;1;yes;;ID here (ex. "2")]
$endif
