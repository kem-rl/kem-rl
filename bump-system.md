Aujourd'hui je vous montre un code assez facile pour bump serveur en BDScript 2 sur BDFD.
Aucune variables.


Trigger : {PREFIXE}bump

$nomention

$sendEmbedMessage[{CHANNEL ID};;Nouveau bump;;> <@$authorID>
> `$authorID`
> a bump ce serveur ! 

> Rejoins le serveur si t'es intéressé !
> *$getServerInvite*;ff0000;;;;;$authorAvatar]



$title[Nouveau bump]
$embeddedURL[https://discord.com/channels/1144231989742936174/1154738026254180352]
$color[ff0000]
$description[
> Le serveur $serverName[$guildID] a été bump par <@$authorID> `$authorID` !

> **Un autre bump sera disponible dans 2 heures !**
]

$globalCooldown[2h;Tu dois attendre 2 heures pour reBump le serveur !]
