Aujourd'hui je vous partage un code pour recréer un salon dans votre serveur
Pas de variables 
Pas d'autres choses à écrires après le nom de la commande.


Trigger : {PREFIXE}nuke

$nomention
$embedSuppressErrors[;**・Une erreur s'est produite lorsque j'ai essayé de nuke.**; 8800d4;;;]
$onlyPerms[managechannels;**・Il vous manque les autorisations suivantes :**
`× Managechannels`.]
$onlyBotPerms[managechannels;**・Il me manque les autorisations suivantes :**
`× Managechannels`.] 
$var[nsfw;$isNSFW[$channelID]]
$var[cate;$parentID]
$var[name;$channelName[$channelID]]
$var[pos;$channelPosition[$channelID]]
$deleteChannels[$channelID]
$createChannel[$channelName[$channelID];text]
$modifyChannel[$findChannel[$var[name]];!unchanged;!unchanged;$var[nsfw];$var[pos];$var[cate]]
$sendEmbedMessage[$findChannel[$var[name]];<@$authorID>;・Nuke;;
*L'utilisateur vient de nuke le salon*
> **Utilisateur**
> <@$authorID> `($authorID)`
> **Temps**
> <t:$getTimestamp:R>;ff0000;;;;;;;yes;no]
