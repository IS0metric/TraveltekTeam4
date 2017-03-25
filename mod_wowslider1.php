<?php
/**
* @title		VisualLightBox gallery module
* @version		1.2.0
* @website		http://www.visuallightbox.com
* @copyright	Copyright (C) 2011 VisualLightBox.com. All rights reserved.
*/

defined('_JEXEC') or die('Restricted access');
$document 			= JFactory::getDocument();
$document->addStyleSheet(JURI::base() . 'modules/mod_'.$module->name.'/engine1/style.css');
$document->addScript(JURI::base() . 'modules/mod_'.$module->name.'/engine1/jquery.js');

require(JModuleHelper::getLayoutPath('mod_'.$module->name));
?>
