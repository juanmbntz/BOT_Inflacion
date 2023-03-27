from datetime import datetime, timedelta
import csv
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np
import time
import requests
import re
from datetime import datetime
import os
#from scripts.scrapper_prices import scrap_prices
#from scripts.calc_increm import calc_increment

# "_test" para pruebas, vacio para prod.
env = ""

def scrap_prices(date_dash, date_nodash):

    urls = [
        
        'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bife-con-lomo-estancias-coto-x-kg/_/A-00047988-00047988-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-descremada-menos-calorias-la-serenisima-botella-larga-vida-1l/_/A-00508910-00508910-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-arroz-largo-fino-gallo-versatil-paquete-1-kg/_/A-00264657-00264657-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-banana-cavendish---xkg/_/A-00000446-00000446-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yogur-bebible-parcialmente-descremado-frutilla-tregar-sch-1-kgm/_/A-00521694-00521694-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-penne-rigate-matarazzo-----paquete-500-gr/_/A-00263765-00263765-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-atun-al-natural-gomes-da-costa-lomo-lata-170-gr/_/A-00123801-00123801-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lomo-de-cerdo-x-kg/_/A-00017613-00017613-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lomo-de-cerdo-cocido-paladini-bli-120-grm/_/A-00284883-00284883-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-servilletas-sussex-ultramax-30x30-paquete-150-unidades/_/A-00230068-00230068-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-servilletas-campanita-soft-33x33-paq-70-uni/_/A-00038048-00038048-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-servilletas-familiares-x-1-sussex-paq-140-uni/_/A-00522551-00522551-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-toallitas-desinfectantes-ayudin-fresco-flowpack-24-un/_/A-00524204-00524204-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-toallitas-desinfectantes-ayudin-limon-flowpack-24-un/_/A-00495037-00495037-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-toallitas-desinfectantes-ayudin-fresco-flowpack-36-un/_/A-00522598-00522598-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-toallitas-desinfectantes-ayudin-limon-doypack-35-un/_/A-00528859-00528859-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-phigienico-x4-rollo-100-c-higienol-paq-40-m2/_/A-00503817-00503817-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-papel-higienico-campanita-soft-plus-xl-simple-hoja-paquete-4-unidades/_/A-00295882-00295882-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bolsas-de-residuos-task-45-x-60-cm-20-u-pequena-multiuso/_/A-00268585-00268585-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-papel-higienico-higienol-max-hoja-simple-panal-paq-4-unid-x-80-mts-c-u/_/A-00531504-00531504-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-phigienico-hoja-simple-x6-elite-paq-18-m2/_/A-00527746-00527746-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lavandina-ayudin-clasica-2-l/_/A-00511456-00511456-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lavandina-ayudin-clasica-botella-4-lts/_/A-00527730-00527730-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lavandina-triple-poder-l-ayudin-bot-2-ltr/_/A-00508209-00508209-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-fidsemolin-c-hvo-nido-n3-308-paq-500-grm/_/A-00479176-00479176-200'
        ,"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-ketchup-hellmann's-regular-250-g-doypack/_/A-00510053-00510053-200"
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tirabuzon-lucchetti-------paquete-500-gr/_/A-00461486-00461486-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-fideos-rigatti-al-huevo-don-vicente-paq-500-grm/_/A-00530597-00530597-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mostachol-lucchetti-----paquete-500-gr/_/A-00265515-00265515-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-fidsemolin-c-hvo-nido-n2-308-paq-500-grm/_/A-00479161-00479161-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lasagna-matarazzo-paq-400-grm/_/A-00525129-00525129-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-harina-de-trigo-blancaflor--0000-paquete-1-kg/_/A-00251435-00251435-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-harina-de-trigo-chacabuco-leudante-paquete-1-kg/_/A-00299169-00299169-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-harina-0000-ultra-refinada-pureza-paq-1-kgm/_/A-00513988-00513988-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-harina-leudante-canuelas-paq-1-kgm/_/A-00528589-00528589-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-harina-trigo-000-blancaflor-1-kg/_/A-00251432-00251432-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-harina-trigo-000-morixe-paq-1-kgm/_/A-00480051-00480051-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jabon-liquido-limpieza-compl-ace-doy-3-ltr/_/A-00521356-00521356-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jabon-liquido-todos-los-dias-woolite-doy-1500-ml/_/A-00490196-00490196-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-suavizante-concentrado-vivere-intense-abrazo-apretado-1-l/_/A-00473538-00473538-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jabon-liquido-ropa-fina-ala-camellito-lavado-a-mano-450-ml/_/A-00263228-00263228-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jabon-liquido-skip-regular-ph-balanceado-800-ml-doypack/_/A-00505657-00505657-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-shampoo-plusbelle-hidratacion-botella-1000-ml/_/A-00266510-00266510-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-shampoo-suave-manzanilla-rubios-930-ml/_/A-00500108-00500108-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-shampoo-suave-lacio-antifrizz-930-ml/_/A-00500096-00500096-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-shampoo-detox-c-bio-pr-plusbelle-bot-1000-ml/_/A-00510646-00510646-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-shampoo-sedal-liso-perfecto-340-ml/_/A-00295231-00295231-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-shampo-ninos-ph-balanceado-plusbelle-bot-700-ml/_/A-00512414-00512414-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-shampo-ninos-sensacion-natu-plusbelle-bot-700-ml/_/A-00512399-00512399-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gomitas-tiburoncitos-frutti-gelatin-bol-30-grm/_/A-00134863-00134863-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gomitas-frut-gel-frutigelati-bsa-30-grm/_/A-00184765-00184765-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gomitas-ositos-mogul-paq-30-grm/_/A-00216569-00216569-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-alfajor-terrabusi-chocolate-50-gr-x-1-uni/_/A-00140272-00140272-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-alfajor-bon-o-bon--40-gr-x-1-uni/_/A-00112646-00112646-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-chocolate-con-leche-c-ma-georgalos-fwp-35-grm/_/A-00509681-00509681-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-chocolate-arcor-chocolate-cja-25-grm/_/A-00165125-00165125-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-chocolate-shot-con-mani-paq-35-grm/_/A-00140301-00140301-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-filtros-papel-n4-melitta-caja-30-unidades/_/A-00294646-00294646-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-te--rosamonte-cja-50-uni/_/A-00011296-00011296-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-te-negro-clasico-x25-so-green-hills-cja-50-grm/_/A-00511777-00511777-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-te-chai-la-virginia-cja-40-grm/_/A-00498134-00498134-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-te-frutilla-la-virginia-est-04-kgm/_/A-00240558-00240558-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-amanda-paquete-500-gr/_/A-00251288-00251288-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-hierbas-serran-chamigo-paq-500-grm/_/A-00484016-00484016-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-te-hierbas-digestivas-cachamai-caja-20-saquitos/_/A-00129303-00129303-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-manzanilla-cruz-de-mal-paq-500-grm/_/A-00488013-00488013-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-instantaneo-torrado-seleccion-arlistan-fra-50-grm/_/A-00259752-00259752-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-4-flex-taragui-1-kg/_/A-00499474-00499474-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-molido-torrado-cabrales-paq-1-kgm/_/A-00061257-00061257-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cappuccino-espuma-de-vainilla-la-virginia-pou-155-grm/_/A-00526405-00526405-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cappuccino-dulce-de-leche-la-virginia-pou-155-grm/_/A-00526401-00526401-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-coffee-mate-liviano-x-170gr/_/A-00243504-00243504-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-instantaneo-arlistan-frasco-170-gr/_/A-00259753-00259753-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-instantaneo-tradicion-nescafe-pou-150-grm/_/A-00505792-00505792-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-instantaneo-suave-la-virginia-fra-170-grm/_/A-00525859-00525859-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-instantaneo-suave-y-espumoso-arlistan-fra-170-grm/_/A-00530603-00530603-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-capsula-chococino-nescafe-dolca-cja-270-grm/_/A-00217282-00217282-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-instantaneo-nescafe-tradicion-x-170-gr/_/A-00282516-00282516-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pure-de-tomate-la-campagnola-tetrabrik-520-gr/_/A-00003234-00003234-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pure-de-tomate-salsati-tetrabrik-520-gr/_/A-00169714-00169714-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pure-de-tomate-coto-con-oregano-tetrabrik-520-gr/_/A-00457065-00457065-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pure-de-tomate-alco---tetrabrik-520-gr/_/A-00208051-00208051-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bizcochos-dulces-gallo-snack-bsa-50-grm/_/A-00262973-00262973-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas--criollitas-paq-300-grm/_/A-00099168-00099168-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas-dulces-anillos-vainilla-9-de-oro-paq-380-grm/_/A-00531289-00531289-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas-mana-livianas-dulces-vainilla-x3-uni-paq-393-grm/_/A-00113665-00113665-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pepas-don-satur-bsa-300-grm/_/A-00282843-00282843-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galldulces-anillos-terrabusi-paq-300-grm/_/A-00531672-00531672-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-variedad-surtidas-terrabusi-paq-390-grm/_/A-00532288-00532288-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gallrellena--opera-paq-92-grm/_/A-00104249-00104249-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gallrellena--rumba-paq-336-grm/_/A-00182503-00182503-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gallrellena-chocolat-melba-paq-360-grm/_/A-00112365-00112365-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas-pepitos-357g/_/A-00532284-00532284-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gallavena-chip-de-chocol-cachafaz-paq-225-grm/_/A-00264081-00264081-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-arveja-seca-rem-inca-lat-350-gr/_/A-00128955-00128955-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-poroto--ciudad-del-lago-de-soja-lata-350-gr/_/A-00281871-00281871-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lentejas-la-campagnola-300-gr/_/A-00494233-00494233-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-garbanzos-la-campagnola-300-gr/_/A-00494235-00494235-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jardinera-inca-350-gr/_/A-00128956-00128956-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-sal-gruesa--celusal-est-1-kgm/_/A-00088714-00088714-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vinagre-alcohol-menoyo-pet-1-ltr/_/A-00007197-00007197-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vinagre-vino-coto-pet-1-ltr/_/A-00059478-00059478-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-sal-entrefina-para-parrilla-celusal-paq-500-grm/_/A-00489264-00489264-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aceite-soja--sojola---botella-900-ml/_/A-00103374-00103374-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aceite-girasol--cocinero---botella-900-ml/_/A-00183553-00183553-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aderezo-ligth-cocinero-clasico-bajo-en-sodio-bot-500-ml/_/A-00242806-00242806-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aderezo-light-cocinero-aceto-y-oliva-pet-500-ml/_/A-00242807-00242807-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aceto-balsamico-reduccion-enrico-baronese-bot-375-cmq/_/A-00532960-00532960-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aceto-balsamico-don-marcell-bot-500-cmq/_/A-00008786-00008786-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aceite-oliva-extra-virgen-natura-intenso-lata-500-ml/_/A-00261936-00261936-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aceite-oliva-extra-virgen-s-cocinero-bot-500-ml/_/A-00515794-00515794-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aceite-rocio-vegetal--canuelas-girasol-aerosol-187-ml/_/A-00484971-00484971-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-avena-instantanea-quaker-cja-660-grm/_/A-00508152-00508152-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerskarchit--granix-bsa-240-grm/_/A-00048071-00048071-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-avena-tradicional-quaker-cja-760-grm/_/A-00508206-00508206-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-avena-tradicional-morixe-paq-300-grm/_/A-00497586-00497586-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-avena-tradicio-coto-paq-400-grm/_/A-00255212-00255212-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cereal-almohaditas-rellenas-sabor-limon-snuks-cja-240-grm/_/A-00515925-00515925-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-musli-cereales-mzana-kellogg-s-cja-270-grm/_/A-00486450-00486450-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-granola-berries-go-natural-paq-250-grm/_/A-00512354-00512354-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cacao-en-polvo-nesquik-x-150gr/_/A-00488014-00488014-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cacao-granulado-chocolino-paq-800-grm/_/A-00525134-00525134-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pure-de-fruta-manzana-zummy-pou-90-grm/_/A-00510049-00510049-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-en-polvo-nutrifuerza-la-lechera-paq-400-grm/_/A-00522399-00522399-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-en-polvo-nido-paq-400-grm/_/A-00522405-00522405-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-en-polvo-nutrifuerza-la-lechera-paq-800-grm/_/A-00522400-00522400-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-edulcorante-con-stevia-chuker-bot-200-ml/_/A-00506257-00506257-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-azucar-rubio-mascabo-ledesma-paq-800-grm/_/A-00481465-00481465-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-azucar-hileret-light-paquete-250-gr/_/A-00119984-00119984-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-edulcorante-sucaryl------botella-360-cc/_/A-00003762-00003762-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-endulzante-clasico-forte-hileret-bot-500-ml/_/A-00511722-00511722-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-edulcorante-clasico-chuker-bot-400-ml/_/A-00506256-00506256-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-endulzante-sweet-forte-hileret-bot-400-ml/_/A-00511706-00511706-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-premezcla-para-tapas-de-alfajores-maizena-paq-400-grm/_/A-00529627-00529627-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-premezcla-hummus-instantaneo-natural-pop-paq-100-grm/_/A-00533404-00533404-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-premezcla-para-chipa-maizena-paq-250-grm/_/A-00529623-00529623-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-arroz-largo-fino-ciudad-del-lago-paquete-1-kg/_/A-00132645-00132645-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-arroz-largo-fino-lucchetti-estuche-x1-kg/_/A-00508839-00508839-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-garbanzos-morixe-paq-400-grm/_/A-00515930-00515930-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-semola-coto-bolsa-400-gr/_/A-00475171-00475171-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-arroz-koshihikari-dos-hermanos-sushi-rice-paquete-500-gr/_/A-00288062-00288062-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-maiz-pisingallo-la-egipciana-bol-400-gr/_/A-00078646-00078646-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lentejas-lonquimay-bolsa-400-gr/_/A-00170564-00170564-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-porotos-manteca-coto-bolsa-500-gr/_/A-00475169-00475169-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lentejon-la-egipciana-seleccion-superior-bol-400-grm/_/A-00078644-00078644-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-poroto-negro-terrasana-bsa-500-grm/_/A-00503032-00503032-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-garbanzo--terrasana-bsa-500-grm/_/A-00502914-00502914-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-arroz-carnaroli--gallo---risotto-a-la-espanola-caja-240-gr/_/A-00264988-00264988-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-arroz-carnaroli--de-cecco-----caja-1-kg/_/A-00211572-00211572-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mayonesa-natura-pouch-950-gr/_/A-00050543-00050543-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mostaza-natura-pouch-500-gr/_/A-00248461-00248461-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mayonesa-danica-pou-500-ml/_/A-00532633-00532633-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-condimento-p-tucos-y-guisos-alicante-sob-25-grm/_/A-00525143-00525143-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-condimento-para-pizza-alicante-sob-25-grm/_/A-00525161-00525161-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mayonesa-danica-pou-250-ml/_/A-00532607-00532607-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mostaza-natura-pouch-250-gr/_/A-00244549-00244549-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salsa-chimichurri-vanoli-picante-pet-350-gr/_/A-00465286-00465286-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salsa-barbacoa-la-parmesana-pet-300-gr/_/A-00267892-00267892-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salsa-de-aji-picante-dos-anclas-pet-375-gr/_/A-00231492-00231492-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salsa-ranch-dos-anclas-pet-420-gr/_/A-00266778-00266778-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salsa-de-soja-dos-anclas---botella-500-ml/_/A-00208310-00208310-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mermelada-durazno-arcor-fra-454-grm/_/A-00521371-00521371-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mermelada-durazno-emeth-pote-420-gr/_/A-00098672-00098672-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mermelada-ciruela-arcor-fra-454-grm/_/A-00520351-00520351-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mermelada-durazno-esnaola-fra-454-grm/_/A-00500587-00500587-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mermelada-ciruela-emeth-frasco-454-gr/_/A-00024586-00024586-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mermelada-light-frutilla-esnaola-fra-390-grm/_/A-00501505-00501505-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mermelada-emeth-maracuya-fra-454-grm/_/A-00248893-00248893-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mermelada-dietetica-arandano-con-stevia-cuartocreciente-fra-300-grm/_/A-00285249-00285249-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-miel-de-abejas-nectar-de-dioses-fra-250-grm/_/A-00288253-00288253-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mermelada-arandanos-el-brocal----frasco-420-gr/_/A-00475555-00475555-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-miel-organica-premi-yunga-andin-fra-470-grm/_/A-00505430-00505430-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bicarbonato-de-sodio-alicante-sob-50-grm/_/A-00527723-00527723-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-provenzal-la-parmesana-paquete-25-gr/_/A-00022963-00022963-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aji-triturado-alicante-sob-25-grm/_/A-00525145-00525145-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-oregano-la-parmesana---sobre-50-gr/_/A-00191237-00191237-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-oregano--valle-de-uc-sob-25-grm/_/A-00493979-00493979-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-condimento-p-chimichurri-la-campagnola-doy-25-grm/_/A-00491193-00491193-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-anis-en-granos-alicante-sob-25-grm/_/A-00526417-00526417-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-comino-molido-alicante-sob-25-grm/_/A-00525866-00525866-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salsa-4-quesos-alicante-sob-37-grm/_/A-00525158-00525158-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-albahaca-la-parmesana-sob-20-grm/_/A-00141418-00141418-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-agua-de-mesa-nestle-bidon-63-l/_/A-00267340-00267340-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-agua-con-gas--benedictino-bot-15-ltr/_/A-00523175-00523175-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-agua-mineral-natural-de-manantial-alvura-225-l/_/A-00477548-00477548-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-agua-sin-gas--ser-bot-225-ltr/_/A-00513679-00513679-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-agua-saborizada-cellier-naranja-botella-15-l/_/A-00262409-00262409-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-mirinda-naranja-bot-15-ltr/_/A-00051816-00051816-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-cunnington----botella-225-l-/_/A-00180413-00180413-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-coca-cola-sin-azucares-2-lt/_/A-00189595-00189595-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-coca-cola-light-2-lt/_/A-00189594-00189594-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-coca-cola-sabor-original-25-lt/_/A-00198715-00198715-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-pepsi-light-black-botella-15-l-/_/A-00467755-00467755-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-coca-cola-sabor-original--3-lt/_/A-00102153-00102153-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-schweppes-sin-azucares-pomelo-225-lt/_/A-00461492-00461492-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-sprite-lima-limon-15-lt/_/A-00016203-00016203-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-coca-cola-light-15-lt/_/A-00008685-00008685-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-agua-saborizada-aquarius-pera-15-lt/_/A-00196409-00196409-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza--santa-fe---botella-1-l/_/A-00082451-00082451-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-tinto--resero-ttb-1-ltr/_/A-00002233-00002233-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-anana-fizz-sin-alcohol-fiesta-de-ninos-bot-1-ltr/_/A-00121517-00121517-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-blanco--toro-ttb-1-ltr/_/A-00514833-00514833-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza-cautiva-rubia-salta-ret-bot-1-l/_/A-00514836-00514836-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza-red-schneider--lata-473-cc/_/A-00485319-00485319-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza-bot-dorada-origina-brahma-bot-710-cmq/_/A-00512691-00512691-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-entera-larga-vida-alimenta-ttb-1-ltr/_/A-00532064-00532064-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-larga-vida-descremada-ciudad-del-lago-ttb-1-l/_/A-00079851-00079851-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-clasica-mas-liviana-la-serenisima-botella-larga-vida-1l/_/A-00508922-00508922-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-multidefensas-0-la-serenisima-sachet-1l/_/A-00511514-00511514-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-parcialmente-descremada-liviana--la-serenisima-larga-vida-1l/_/A-00509747-00509747-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-con-hierro-la-serenisina-botella-larga-vida-1l/_/A-00508909-00508909-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-protein-la-serenisina-botella-larga-vida-1l/_/A-00508911-00508911-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-silk-almendra-con-chocolate-946-ml/_/A-00493165-00493165-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bebida-vegetal-granola-la-serenisima-ttb-1-ltr/_/A-00518042-00518042-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-la-serenisima-100-vegetal-almendra-1l/_/A-00498602-00498602-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapempanada-criolla-x20-mendia-bsa-520-grm/_/A-00258362-00258362-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapempanada-hojaldre-mendia-fwp-520-grm/_/A-00251644-00251644-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapa-p-pascualina--coto-bol-400-grm/_/A-00026582-00026582-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapempanada-horno-ciudad-del-lago-bsa-300-grm/_/A-00024171-00024171-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-ravioles-ricota-mendia-bsa-1-kgm/_/A-00468762-00468762-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jamon-cocido-clasico-fetead-lario-x-kg/_/A-00013380-00013380-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jamon-cocido-espanol-fetead-el-pozo-xkg-1-kgm/_/A-00011864-00011864-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lomo-feteado-paladini--1-kgm/_/A-00045192-00045192-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lomo-horneado-fetea-bocatti--1-kgm/_/A-00046139-00046139-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lomo-de-cerdo-cocido-paladini-bli-120-grm/_/A-00284883-00284883-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dce-batata-con-chocolate--1-kgm/_/A-00045802-00045802-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-de-batata-esnaola-cja-500-grm/_/A-00004139-00004139-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-de-batata-arcor-cja-500-grm/_/A-00070360-00070360-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-crema-light-la-serenisima-pot-290-grm/_/A-00528605-00528605-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-crema-la-paulina-tradicional-290-gr/_/A-00212429-00212429-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-untable-la-paulina-clasico-190-gr/_/A-00174397-00174397-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-blanco-clasico-tregar-pot-290-grm/_/A-00511747-00511747-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-blanco-light-tregar-pot-290-grm/_/A-00511751-00511751-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-untable-tentaciones-4--tholem-pot-190-grm/_/A-00255982-00255982-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-casancrem-entero-200-gr/_/A-00504139-00504139-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-zapallo-japones---xkg/_/A-00017625-00017625-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-naranja-comercial---xkg/_/A-00061006-00061006-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-zapallo-anco-x-kg/_/A-00000688-00000688-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-papa-negra-selec---xkg/_/A-00060947-00060947-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-batata-americana---xkg-1-kgm/_/A-00072044-00072044-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-papa-blanca----xkg/_/A-00000695-00000695-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-choclo-amarillo---xkg/_/A-00000614-00000614-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limon-comercia---xkg/_/A-00061007-00061007-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-choclo-especial-x-kg---xkg/_/A-00035090-00035090-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cebolla-a-granel-x-kg/_/A-00000602-00000602-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-ciruela-x-kg/_/A-00063594-00063594-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-brocoli-x-kg/_/A-00000598-00000598-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-manzana-red----xkg/_/A-00000529-00000529-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-manzanagsmith----xkg/_/A-00000527-00000527-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-manzana-red-elegida-x-kg/_/A-00000528-00000528-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aji-picante-----xkg/_/A-00000696-00000696-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-kiwi-seleccion---x-kg/_/A-00000496-00000496-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-roast-beef-estancias-coto-x-kg/_/A-00047985-00047985-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-chorizo-fco-bombon-fridevi--1-kgm/_/A-00011645-00011645-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bondiola-de-cerdo-finas-hierbas-x-kg/_/A-00011943-00011943-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-asado-del-medio-estancias-coto-x-kg/_/A-00047979-00047979-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bife-angosto-estancias-coto-x-kg/_/A-00047987-00047987-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-milanesa-bola-de-lomo-estancias-coto-x-kg/_/A-00047993-00047993-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-peceto--estancias-coto-x-kg/_/A-00047994-00047994-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-nalga-estancias-coto-x-kg/_/A-00047991-00047991-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bife-con-lomo-estancias-coto-x-kg/_/A-00047988-00047988-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-entrana-estancias-coto-x-kg/_/A-00047982-00047982-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-matambre-estancias-coto-x-kg/_/A-00047996-00047996-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salmon-rosado-fresco-trozado--x-1-kgm/_/A-00013120-00013120-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-filete-de-merluza-despinado-fresco-x-kg/_/A-00017834-00017834-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-filete-de-lenguado-fresco-x-kg/_/A-00017841-00017841-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pata-con-piel-x-uni-(450-gr)-refrigerados/_/A-00048535-00048535-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-alitas-x-uni-(455-gr)/_/A-00048445-00048445-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pollo-congelado-x-kg/_/A-00042989-00042989-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pata-muslo-con-piel-x-uni-(14-kg)-refrigerados/_/A-00048458-00048458-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-supremas-sin-piel-x-uni-(960-gr)-refrigerados/_/A-00048480-00048480-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-huevo-blanco--el-ombu-map-30-uni/_/A-00014052-00014052-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-huevo-blanco-grand-maple-x-30-uni-30-uni/_/A-00032342-00032342-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-huevo-color-grande-el-ombu-map-30-uni/_/A-00059720-00059720-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-huevo-color-maple-x-30-uni-30-uni/_/A-00036411-00036411-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-huevo-color-grande-el-ombu-cja-12-uni/_/A-00012334-00012334-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-huevo-color--cja-12-uni/_/A-00022878-00022878-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-medallones-burger-swift---4-uni-x-69-gr--/_/A-00166470-00166470-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-hamburguesa-carne-vacuna-x-swift-cja-276-grm/_/A-00513718-00513718-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-hamburguesas-swift--12-uni-x-80-gr-clasicas/_/A-00290730-00290730-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-milanesa-soja-tcasero-granja-del-paq-330-grm/_/A-00258818-00258818-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-milanesas-soja-lucchetti-x-290-grm/_/A-00256598-00256598-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-milanesas-soja-x4-lucchetti-paq-560-grm/_/A-00515414-00515414-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-milanesa-soja-tipo-casero-x-granja-del-paq-660-grm/_/A-00258821-00258821-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-desod-ambiente-espiritu-play-poett-aer-360-ml/_/A-00510571-00510571-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-desod-ambiente-flores-de-prim-poett-aer-360-ml/_/A-00508180-00508180-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-desodorante-de-ambiente-harmony-glade-aer-360-cmq/_/A-00528884-00528884-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-desinfectante-amanecer-de-mo-odex-aer-360-ml/_/A-00487182-00487182-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-sopapa-de-goma-x-limp-negra-con-cabo-1-uni/_/A-00267331-00267331-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpiador-ecovita-bano-doy-500-ml/_/A-00281920-00281920-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpiador-en-crema-cif-limon-multiuso-250-ml/_/A-00501823-00501823-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpiador-de-bano-lysoform-liquido-repuesto-450ml/_/A-00487965-00487965-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpiador-liquido-cif-bano-biodegradable-500-ml-gatillo/_/A-00503772-00503772-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpiador-bano-bio-active-cif-gat-500-ml/_/A-00531067-00531067-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpiador-de-bano-lysoform-liquido-gatillo-500ml/_/A-00180420-00180420-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpia-inodoros-desinfectante-lysoform-gel-active-power-lavanda-500ml/_/A-00495843-00495843-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-canasta-liquida-para-inodoro-glade-i-love-you-aparato--repuesto-50ml/_/A-00272254-00272254-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-detergente-finish-----botella-/_/A-00458973-00458973-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lavavajillas-bio-actlima-cif-bot-500-ml/_/A-00531065-00531065-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpiador-antigrasa-extra-power-cocina-mrmusculo-gat-500-cmq/_/A-00531975-00531975-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-sal-regeneradora-glow-bot-1-kgm/_/A-00508186-00508186-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lavavajillas-multiuso-naran-magistral-bot-750-ml/_/A-00519965-00519965-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limppisos-lavanda-ecovita-bot-900-cmq/_/A-00468412-00468412-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpiador-liquido-multisuperficies-glade-campos-de-lavanda-botella-18l/_/A-00267413-00267413-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpiador-procenex-marina-bid-5-lts/_/A-00264345-00264345-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpiador-pinoluz-pino-larga-duracion-bot-1800-cc/_/A-00266008-00266008-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpiador-desinfectante-ayudin-marina-botella-18-l/_/A-00512942-00512942-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpliquido-vidrios-secado-procenex-doy-420-ml/_/A-00297748-00297748-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bolsas-de-residuos-task-45-x-60-cm-20-u-pequena-multiuso/_/A-00268585-00268585-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bolsas-de-polietileno-trash-45-x-60-cm-30-u-multiuso/_/A-00503117-00503117-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bolsa-resid-45-x-60-task-paq-20-uni/_/A-00295873-00295873-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bolsas-de-residuos-task-50-x-70-cm-20-u-multiuso/_/A-00268583-00268583-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cepillo-dental-adulto-sustent-2life-paq-1-uni/_/A-00510295-00510295-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cepillo-dental-infantil-suste-2life-paq-1-uni/_/A-00510294-00510294-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cepillo-dental-colgate-triple-accion-medio-2unid/_/A-00224342-00224342-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cepillo-dental-colgate-extra-clean-medio-1unid/_/A-00121625-00121625-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-crema-dental-colgate-sensitive-pro-alivio-50g/_/A-00211694-00211694-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-crema-dental-sensodyne-blanqueador-extra-fresh-pomo-50-gr/_/A-00200883-00200883-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-enjuague-bucal-listerine-cool-24hs-x250ml/_/A-00185347-00185347-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-enjuague-bucal-colgate-plax-fresh-mint-250ml/_/A-00259253-00259253-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pasta-dental-anti-caries-oral-b-cja-150-uni/_/A-00521854-00521854-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pasta-dental-colgate-herbal-140g/_/A-00503686-00503686-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-toallitas-humedas-para-bebe-johnsons-hora-del-sueno-x-96-un/_/A-00267868-00267868-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-toallitas-humedas-baby-dove-humectacion-enriquecida-50-unidades/_/A-00299671-00299671-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-acondicionador-para-ninos-suave-frutilla-glamorosa-350-ml/_/A-00243270-00243270-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-sh-p-bebe-extra-suave-algabo-bot-444-ml/_/A-00169044-00169044-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-acondicionador-para-ninos-suave-manzanilla-talentosa-350-ml/_/A-00283948-00283948-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-crema-de-calendula-bushi-bushi-cja-50-grm/_/A-00128664-00128664-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-shampoo-para-bebe-johnsons-cabello-claro-x-750-ml/_/A-00510318-00510318-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jabon-en-barra-baby-dove-humectacion-enriquecida-75-g/_/A-00299665-00299665-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-shampoo-para-ninos-johnsons-hidratacion-intensa-x-200-ml/_/A-00514409-00514409-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jabon-suavidad-natur-estrella-ba-paq-75-grm/_/A-00489973-00489973-200'
        ,"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-crema-hidratante-para-bebe-johnson's-recien-nacido-x-200-ml/_/A-00282036-00282036-200"
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-acondicionador-largo-saludabl-plusbelle-bot-970-ml/_/A-00510608-00510608-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-acondicionador-hidratacion-aguacate-y-argan-algabo-doy-300-ml/_/A-00528816-00528816-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-acondicionador-bomba-de-nutricion-sedal-bot-650-ml/_/A-00525574-00525574-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-acondicionador-dove-ritual-de-reparacion-coco-y-curcuma-750-ml/_/A-00513603-00513603-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-acondicionador-oil-repair-3-recarga-nutritiva-garnier-fructis-bot-650-ml/_/A-00517979-00517979-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-crema-corporal-hiratacion-profunda-villeneuve-bot-400-ml/_/A-00526589-00526589-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-crema-corporal-st-ives-avena-y-karite-350-ml/_/A-00262123-00262123-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-crema-hinds-cuerpo-hidratante-piel-normal-vit-alo-bot-350m/_/A-00265973-00265973-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-crema-corporal-mas-hidratacion-villeneuve-bot-250-ml/_/A-00526576-00526576-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-crema-corporal-st-ives-humectacion-diaria-350-ml/_/A-00262125-00262125-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-crema-hinds-hidratacion-esencial-piel-normal-bot-250ml/_/A-00265972-00265972-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-crema-corporal-dove-nutricion-esencial-200-ml/_/A-00251633-00251633-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-colonia-colbert-us-cja-60-ml/_/A-00174784-00174784-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-colonia-para-ninos-mujercitas-cja-80ml/_/A-00261301-00261301-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-colonia-kevin-vert-cja-60-ml/_/A-00174899-00174899-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-maquina-de-afeitar-gillette-prestobarba3---blister-2-unidades/_/A-00189540-00189540-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-repuestos-para-afeitar-gillette-mach3-6-unidades/_/A-00506718-00506718-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-maquina-afeitar-prestobarba-3-sensitive-gillette-bli-8-uni/_/A-00532634-00532634-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-maquina-afeitar-prestobarba-2-untragrip-plus-gillette-paq-5-uni/_/A-00532578-00532578-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-banda-depilat-axilas-area-bi-veet-cja-16-uni/_/A-00502558-00502558-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pinza-para-depilar-tao-decorada-paq-1-uni/_/A-00226475-00226475-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cera-depilatoria-perlas-vegetal-millefiori-fwp-100-grm/_/A-00503554-00503554-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cera-depilatoria-vegetal-millefiori-lat-200-grm/_/A-00503555-00503555-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-crema-depil-piel-sensible-veet-est-100-ml/_/A-00180129-00180129-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-entera-3-tenor-graso-lechelita-sch-1-ltr/_/A-00518044-00518044-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yogur-bebible-entero-vainilla-lechelita-sch-900-grm/_/A-00527826-00527826-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-manteca-tonadita-baja-en-lactosa-200-gr/_/A-00481466-00481466-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-manteca-tonadita-baja-en-lactosa-200-gr/_/A-00481466-00481466-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-manteca-multivitaminas-la-serenisima-200gr/_/A-00495534-00495534-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-rollo-de-cocina-campanita-180-panos-paquete-3-unidades/_/A-00224749-00224749-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-suave-playadito-500-gr/_/A-00502007-00502007-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-azucar-superior-real-ledesma-paq-1-kgm/_/A-00218834-00218834-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-variedad-surtidas-terrabusi-paq-170-grm/_/A-00532286-00532286-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas-crackers-clasicas-express-paq-101-grm/_/A-00521346-00521346-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-blanco-fargo-rodajas-finas-bsa-560-grm/_/A-00268428-00268428-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-de-mesa-blanco-lactal-bsa-500-grm/_/A-00530650-00530650-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-blanco--bimbo-bsa-550-grm/_/A-00495379-00495379-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jamon-cocido-feteado-primera-marc-xkg/_/A-00035168-00035168-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-de-maquina--xkg-1-kgm/_/A-00040612-00040612-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-muzzarella--dona-aurora-xkg/_/A-00019971-00019971-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-huevo-blanco-grand--cja-12-uni/_/A-00022865-00022865-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-hamburguesas-swift--12-uni-x-80-gr-clasicas/_/A-00290730-00290730-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tirabuzon-lucchetti-------paquete-500-gr/_/A-00461486-00461486-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pure-de-tomate-salsati-tetrabrik-520-gr/_/A-00169714-00169714-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pulpa-de-tomate-salsati-tetrabrik-520-gr/_/A-00169716-00169716-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapa-p-pascualina-sin-tacc-la-saltena-fwp-380-grm/_/A-00470274-00470274-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-harina-trigo-000-morixe-paq-1-kgm/_/A-00480051-00480051-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-agua-mineralizada-artificialmente-con-gas-bajo-en-sodio-cellier-2-l/_/A-00479242-00479242-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas--criollitas-paq-300-grm/_/A-00099168-00099168-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas-crackers-clasicas-media-tarde-pack-familiar-x3-unidades-paq-315-grm/_/A-00532069-00532069-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-alfajor-jorgito-blanco-50-gr-x-6-uni/_/A-00118365-00118365-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-alfajor-terrabusi-chocolate-50-gr-x-1-uni/_/A-00140272-00140272-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-alfajor-de-arroz-ddl-vauquita-fwp-28-grm/_/A-00501493-00501493-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-alfajor-d-arroz-ddl-chocoarroz-fwp-22-grm/_/A-00513635-00513635-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mini-alfajor-negro-jorgito-fwp-155-grm/_/A-00118370-00118370-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-alfajor-tofi-chocolate-46-gr-x-6-uni/_/A-00471470-00471470-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-alfajor-milka-oreo-chocolate-61-gr-x-1-uni/_/A-00267716-00267716-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-caramelos-strong-menthoplus-paq-294-grm/_/A-00216702-00216702-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-caramelos-sugus-confitados-50-grs/_/A-00112649-00112649-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-caramelos-tfruti-flynn-paff-paq-504-grm/_/A-00090080-00090080-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-caramelos-billiken-yogurt-bol-600-grm/_/A-00014007-00014007-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-caramelos-mogul-gusanito-mogul-paq-500-grm/_/A-00201438-00201438-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pastillero-tic-tac-sabor-sandia-pas-16-grm/_/A-00523184-00523184-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-chicles-topline-menta-paq-67-grm/_/A-00193948-00193948-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-chicles-topline-seven-menta-paq-14-grm/_/A-00243610-00243610-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-azucar-mascabo-arcor-paq-500-grm/_/A-00493534-00493534-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-endulzante-clasico-forte--hileret-cja-50-grm/_/A-00513659-00513659-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-endulzante-forte-stevia-5-hileret-cja-50-grm/_/A-00517958-00517958-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-edulcorante-clasico-chuker-bot-400-ml/_/A-00506256-00506256-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-hierbas-serranas-chamigo-paq-500-grm/_/A-00530602-00530602-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-4-flex-taragui-500-gr/_/A-00499473-00499473-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-suave-playadito-1-kg/_/A-00502038-00502038-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-4-flex-taragui-1-kg/_/A-00499474-00499474-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-4-flex-union-1-kgm/_/A-00512930-00512930-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-hierbas-serran-cbse-paq-1-kgm/_/A-00512968-00512968-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-guarana-cbse-paq-500-grm/_/A-00512966-00512966-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-suave-amanda-paq-1-kgm/_/A-00511470-00511470-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-suave-amanda-paq-500-grm/_/A-00511503-00511503-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-playadito-paquete-500-gr/_/A-00269852-00269852-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-canarias-paquete-1-kg/_/A-00135321-00135321-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-te--rosamonte-cja-50-uni/_/A-00011296-00011296-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-te-verde-citrus-la-virginia-est-20-uni/_/A-00240741-00240741-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-te-x100-saq-filtr-taragui-est-100-uni/_/A-00511774-00511774-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-te-verde-la-virginia-----caja-20-saquitos/_/A-00239153-00239153-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-te-ilumine-inti-zen-est-15-uni/_/A-00164910-00164910-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-te-x25-saquitos-la-virginia-cja-50-grm/_/A-00516582-00516582-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-te-negro-clasico-x25-so-green-hills-cja-50-grm/_/A-00511777-00511777-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-te-c-sablimon-green-hills-x-20-uni/_/A-00500124-00500124-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-molido-coto-paquete-250-gr/_/A-00125960-00125960-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-molido-la-virginia----paquete-250-gr/_/A-00230124-00230124-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-molido-torrado-intens-morenita-paq-250-grm/_/A-00514043-00514043-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-molido-torrado-equilibrado-la-virginia-paq-1-kgm/_/A-00532308-00532308-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-torrado-molido-bonafide-paquete-1-kg/_/A-00025064-00025064-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-torrado-molido-bonafide-suave-paquete-250-gr/_/A-00038447-00038447-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-molido-torrado-cabrales-paq-1-kgm/_/A-00061257-00061257-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cappuccino-sabor-mousse-de-chocolate-y-avellanas-la-virginia-pou-155-grm/_/A-00526413-00526413-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cappuccino-morenita-doy-125-grm/_/A-00527728-00527728-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-molido-tostado-martinez-suave-paq-250-grm/_/A-00286074-00286074-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-instantaneo-sabor-caramelo-nescafe-125-grm/_/A-00536714-00536714-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-tostado-molido-super-cabrales-paq-250-grm/_/A-00032787-00032787-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-instantaneo-original-nescafe-fra-170-grm/_/A-00522417-00522417-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-instantaneo-nescafe-tradicion-x-170-gr/_/A-00282516-00282516-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-capsulas-nescafe-dolca-160-grm/_/A-00502020-00502020-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-capsulas-cappuccino-espresso-la-virginia-cja-60-grm/_/A-00533395-00533395-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mate-cocido-x100-saq-sele-la-tranquer-cja-400-grm/_/A-00511576-00511576-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-flautita-congelada-x-unidad/_/A-00012179-00012179-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pizzetas-de-tomate-coto/_/A-00044091-00044091-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-madialuna-de-manteca/_/A-00000937-00000937-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-mesa-lacteado-con-l-sacaan-bsa-580-grm/_/A-00468720-00468720-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-de-mesa-blanco-lactal-bsa-500-grm/_/A-00530650-00530650-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-baguette-x-unidad/_/A-00011615-00011615-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-con-salvado-lactal-bsa-600-grm/_/A-00530648-00530648-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-salvado-pan-de-graham--sacaan-bsa-350-grm/_/A-00468721-00468721-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-blanco--bimbo-bsa-550-grm/_/A-00495379-00495379-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-para-hamburguesas-x4-uni-saacan-bsa-210-grm/_/A-00517981-00517981-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tortilla-mexicana-tia-rosa-bsa-320-grm/_/A-00296211-00296211-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-integral-mix-cereal-fargo-bsa-430-grm/_/A-00488375-00488375-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-blanco-bimbo-artesano-500g/_/A-00293087-00293087-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-linea-dorada-multicereal-noly-bsa-540-grm/_/A-00498125-00498125-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-p-pancho-corto-mendia-bsa-210-grm/_/A-00481476-00481476-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-semillado-con-avena-y-mi-bimbo-paq-600-grm/_/A-00190705-00190705-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-rapiditas-ligh-bimbo-paq-275-grm/_/A-00180228-00180228-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pan-de-hamburguesa-bimbo-artesano-4u-240-grm/_/A-00457147-00457147-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas-mana-livianas-dulces-vainilla-x3-uni-paq-393-grm/_/A-00113665-00113665-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas-dulces-anillos-vainilla-9-de-oro-paq-380-grm/_/A-00531289-00531289-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas-dulces-pepas-tia-maruca-paq-180-grm/_/A-00530614-00530614-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gall-agua-de-agua-la-providen-paq-303-grm/_/A-00469832-00469832-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gall-agua---ciudad-del--paq-330-grm/_/A-00136910-00136910-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galldulces-surtido-diversion-paq-390-grm/_/A-00510874-00510874-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gallcrackers-5-semillas-coto-paq-250-grm/_/A-00484445-00484445-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pepas-membrillo-trio-paq-500-grm/_/A-00219742-00219742-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galldulces-vainilla-vocacion-paq-141-grm/_/A-00511496-00511496-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gallrellena-vainilla-rell-polvorita-paq-147-grm/_/A-00485720-00485720-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas-cerealitas-clasicas-621gr/_/A-00532290-00532290-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galldulces-surtido-bagley-paq-390-grm/_/A-00511763-00511763-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pepas-c-membrllo-nat-9-de-oro-bsa-380-grm/_/A-00468005-00468005-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galldulces-chocolat-chocolinas-paq-250-grm/_/A-00034482-00034482-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galldulces-sabor-coco-9-de-oro-paq-120-grm/_/A-00493122-00493122-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gallrellena-opera-opera-pak-220-grm/_/A-00015889-00015889-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas-express-clasicas-303gr/_/A-00521329-00521329-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gallcrackers-mini-sadwich-don-satur-bsa-250-grm/_/A-00473723-00473723-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas-rellenas-mellizas-paq-336-grm/_/A-00182498-00182498-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gallrellena-chantily-amor-paq-336-grm/_/A-00182505-00182505-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gallsalvado-dulce-granix-paq-500-grm/_/A-00002545-00002545-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-oblea-milka-bis-oreo-1056-grs/_/A-00491035-00491035-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gallrellena-sab-chocolate-macucas-paq-110-grm/_/A-00508168-00508168-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gallrellena-frutilla-merengadas-paq-93-grm/_/A-00183014-00183014-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gallsin-sal--granix-paq-185-grm/_/A-00001099-00001099-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galldulces-avena-con-chip-granix-paq-255-grm/_/A-00202795-00202795-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gallrellena-sab-frambuesa-sonrisas-paq-324-grm/_/A-00511473-00511473-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galldulces-chips-d-chocol-terrabusi-paq-144-grm/_/A-00515002-00515002-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas-oreo-354g/_/A-00532300-00532300-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas-pepitos-119g/_/A-00532285-00532285-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mostaza-menoyo-pou-250-grm/_/A-00517968-00517968-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-mostaza-savora-original-500-g/_/A-00517488-00517488-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-ketchup-la-campagnola-250-grm/_/A-00260936-00260936-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-ketchup-hot-la-campagnola-250-grm/_/A-00260935-00260935-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salsa-golf-natura-pouch-250-gr/_/A-00244505-00244505-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-arvejas-secas-remojadas-tarragona-340-grm/_/A-00534736-00534736-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-choclo-amarillo-cremoso-tarragona-340-grm/_/A-00534733-00534733-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-arvejas-secas-arcor-300-grm/_/A-00532713-00532713-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-garbanzos-secos-remojados-ciudad-del-lago-300-grm/_/A-00526256-00526256-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jardinera-inalpa-lat-300-grm/_/A-00531531-00531531-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lentejas-remojadas-la-banda-340-grm/_/A-00538026-00538026-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-champignones-en-trozos-al-natural-bahia-184-grm/_/A-00536387-00536387-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-champignon-en-trozos-ciudad-del-lago-lata-400-gr/_/A-00039644-00039644-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-palmitos-enteros-ciudad-del-lago-lata-800-gr/_/A-00170032-00170032-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pepinitos-en-vinagre-castell---pouch-300-gr/_/A-00173804-00173804-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-atun-al-natural--ciudad-del-lago-desmenuzado-lata-170-gr/_/A-00070701-00070701-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-atun-lomo-atun-cla--gomes-da-co-lat-170-grm/_/A-00184869-00184869-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lomo-natural-bajo-en-sodio-gomes-da-costa-lat-170-grm/_/A-00515899-00515899-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-atun-en-aceite-gomes-da-costa-lomitos-lata-170-gr/_/A-00123799-00123799-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lomitos-de-atun-en-agua-con-jugo-de-limon-robinson-crusoe-lat-155-grm/_/A-00523600-00523600-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-atun-en-aceite-coto-lomitos-lata-165-gr/_/A-00179551-00179551-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-ensalada-de-quinoa-con-atun-robinson-crusoe-lat-160-grm/_/A-00523594-00523594-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-durazno-ciudad-del-lago-lata-820-gr/_/A-00014245-00014245-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-durazno-coto-lata-820-gr/_/A-00059623-00059623-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-anana-ciudad-del-lago-lata-850-gr/_/A-00060492-00060492-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pate-foie-swift-lat-90-gr/_/A-00002644-00002644-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-frutos-secos-mani-tostado-con-tomate-y-albahaca-natural-break-fwp-30-grm/_/A-00525285-00525285-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-frutos-secos-mani-tostado-con-sal-y-azucar-mascabo-natural-break-fwp-120-grm/_/A-00520486-00520486-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-avena-tradicio-coto-paq-400-grm/_/A-00255212-00255212-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-avena-tradicional-quaker-760-grm/_/A-00508206-00508206-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-avena-instantanea-morixe-paq-600-grm/_/A-00497577-00497577-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-barras-arroz-limon-x3-uni-crowie-paq-36-grm/_/A-00503901-00503901-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-barra-brownie-laddubar-30-gr/_/A-00511047-00511047-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cereal-frutal-trix-480-grm/_/A-00522573-00522573-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-barra-de-cereal-cereanola-manzana-6-uni-est-126-grm/_/A-00164871-00164871-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-barra-cereal-mousse-de-chocolate-quaker-156-grm/_/A-00186165-00186165-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cereal-c-fruta---flow-est-138-grm/_/A-00169412-00169412-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-barra-cereal-light-yoghurt-cereal-mix-104-grm/_/A-00536069-00536069-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-barra-cereal-frutas-y-f-se-nature-vall-cja-210-grm/_/A-00484024-00484024-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-barra-cereal-original-cereal-mix-92-grm/_/A-00536460-00536460-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jugo-cepita-del-valle-manzana-1-lt/_/A-00503179-00503179-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aceitunas-verdes-castell-650-gr/_/A-00498800-00498800-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aceitunas-verdes-nucete-------sachet-800-gr/_/A-00184783-00184783-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jugo-cepita-del-valle-fresh-pomelo-15-lt/_/A-00495550-00495550-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jugo-polvo-naranja-arcor-sob-18-grm/_/A-00511828-00511828-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jugo-cepita-del-valle-naranja-tentacion-1-lt/_/A-00297931-00297931-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-ades-soja--jugo-de-naranja-1-lt/_/A-00256105-00256105-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tang-frutilla-vitaminas-cd-18grm/_/A-00531996-00531996-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jugo-naranja-arcor-ttb-200-ml/_/A-00489934-00489934-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jugo-c-pulpa-naranja-valen-citric-ttb-15-l/_/A-00503631-00503631-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-amargo-tres-torres-light-blanco-botella-15-l/_/A-00268274-00268274-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-amargo-terma-pomelo-rosado-botella-175-l/_/A-00257436-00257436-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-amargo-terma-light-limon-cero-botella-135-l/_/A-00288546-00288546-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bebida-energizante-monster-mango-loco-473-ml/_/A-00490207-00490207-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-energizante-red-bull-355-ml/_/A-00486126-00486126-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-energizante-speed-unlimited-269-ml/_/A-00534755-00534755-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-cunnington-sin-azucar-naranja-botella-225-l-/_/A-00199815-00199815-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-schweppes-tonica-225-lt/_/A-00243476-00243476-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza--isenbeck---botella-1-l/_/A-00243261-00243261-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza--quilmes---porron-340-cc/_/A-00271680-00271680-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza--santa-fe---botella-1-l/_/A-00082451-00082451-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza-pilsener-iguana---botella-1-l/_/A-00129407-00129407-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza--quilmes---botella-1-l/_/A-00238214-00238214-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza--brahma---botella-1-l/_/A-00238215-00238215-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza-lager-amstel---botella-1-l/_/A-00503972-00503972-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza-pilsen-santa-fe-lat-473-cmq/_/A-00514828-00514828-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza--quilmes-cristal-pack-latas-473-cc-6-unidades/_/A-00204113-00204113-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza-blonde-santa-fe---lata-473-cc/_/A-00475825-00475825-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza--andes--botella-1-l/_/A-00478431-00478431-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-colon-cabernet-sauvignon-botella-de-750-ml/_/A-00016387-00016387-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-tinto-clasico-goyenechea-bot-750-ml/_/A-00004845-00004845-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-cabernet-sauvignon-est-mendoza-bot-750-cc/_/A-00164980-00164980-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-malbec-novecento-bot-750-cc/_/A-00166257-00166257-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-syrah-finca-las-moras-bot-750-cmq/_/A-00141628-00141628-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-sauvign-blanc-finca-las-m-bot-750-cmq/_/A-00180844-00180844-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-malbec-finca-las-moras-bot-750-cc/_/A-00034537-00034537-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-syrah-alaris-trapiche-bot-750-cc/_/A-00141627-00141627-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-merlot--trapiche-bot-750-cmq/_/A-00080016-00080016-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-frosad-dulce-finca-las-m-bot-750-ml/_/A-00286025-00286025-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-eugenio-busto-leyenda-cabernet-sauvignon-750-cc-/_/A-00461091-00461091-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-red-blend-aime-x750-ml/_/A-00298540-00298540-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza-lager-stella-artois---botella-975-cc/_/A-00164527-00164527-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza-blend-salta-lat-473-cmq/_/A-00525869-00525869-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-pinot-noir-el-portillo-bot-750-ml/_/A-00475821-00475821-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-cabernet-sauvignon-san-felipe-s-madera-bot-750-cc/_/A-00183157-00183157-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-malbec-marcus-bot-750-cc/_/A-00160074-00160074-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-red-blend--fuzion-bot-750-ml/_/A-00501983-00501983-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vino-chardonnay-nieto-senetiner-x750-ml/_/A-00052492-00052492-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-champana-e-b-reserve-cuvee-mumm-bot-750-cmq/_/A-00186471-00186471-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-espumante-apertif-chandon-bot-750-ml/_/A-00510549-00510549-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-espumante-demi-sec-chandon-bot-750-ml/_/A-00510544-00510544-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-descremada-coto-sachet-1-l/_/A-00010491-00010491-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-larga-vida-descremada-ciudad-del-lago-ttb-1-l/_/A-00079851-00079851-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-descremada-menos-calorias-la-serenisima-sachet-1l/_/A-00483365-00483365-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-deslv-uat-yatasto-ttb-1000-cmq/_/A-00474513-00474513-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-descremada-la-serenisima-1-sachet-1-l/_/A-00290385-00290385-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-larga-vida-entera-tregar-ttb-1-l/_/A-00262249-00262249-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-larga-vida-descremada-veronica-ttb-1-l/_/A-00081545-00081545-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-multidefensas-0-la-serenisima-sachet-1l/_/A-00511514-00511514-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-entera-larga-vida-uat-extra-defensas-las-tres-ninas-1-ltr/_/A-00510056-00510056-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-parcialmente-descremada-larga-vida-ilolay-ttb-1-ltr/_/A-00527742-00527742-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-parcialmente-descremada-liviana-la-serenisima-botella-larga-vida-1l/_/A-00508916-00508916-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-protein-la-serenisina-botella-larga-vida-1l/_/A-00508911-00508911-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-chocolatada-sin-azucar-nesquik-200-ml/_/A-00532265-00532265-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-infantil--1-ano-nan-190-ml/_/A-00535186-00535186-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-infantil--1-ano-nan-190-ml/_/A-00535186-00535186-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yogur-bebible-entero-coto-frutilla-1-ltr/_/A-00100482-00100482-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yogur-bebible-parcialmente-descremada-vainilla-milkaut-sch-125-kgm/_/A-00519755-00519755-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-leche-clasico-tonadita-pot-1-kgm/_/A-00515698-00515698-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-de-leche-coto-pote-400-gr/_/A-00285028-00285028-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-leche-repostero-coto-pot-400-grm/_/A-00011491-00011491-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-leche-de-campo-milkaut-pot-400-grm/_/A-00532582-00532582-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-leche-tradicion-san-ignacio-pot-410-grm/_/A-00525206-00525206-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-de-leche-la-serenisima-estilo-colonial-1-kg/_/A-00251947-00251947-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-leche-clasico-sancor-pot-400-grm/_/A-00226340-00226340-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-de-leche-clasico-la-serenisima-400gr/_/A-00251874-00251874-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-leche-clasico-ilolay-pot-405-grm/_/A-00527740-00527740-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-leche-repostero-milkaut-pot-405-grm/_/A-00513729-00513729-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-de-leche-vacalin-pote-400-gr/_/A-00227698-00227698-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-margarina-margadan-light-500-gr/_/A-00011272-00011272-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-margarina-delicia-200-grm/_/A-00262259-00262259-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-manteca-ciudad-del-lago-200-gr/_/A-00066423-00066423-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-producto-untable-armonia-pan-200-grm/_/A-00528833-00528833-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-manteca-coto-200-gr/_/A-00008898-00008898-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-manteca-calidad-extra-primer-premio-pan-500-grm/_/A-00002696-00002696-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-manteca-sin-sal-conaprole-paq-200-grm/_/A-00083573-00083573-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-manteca-veronica-200-gr/_/A-00011733-00011733-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-manteca-con-crema-la-serenisima-pan-200-grm/_/A-00533015-00533015-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-manteca-multivitaminas-la-serenisima-200gr/_/A-00495534-00495534-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-estofado-de-cerdo-x-kg/_/A-00047597-00047597-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-roast-beef-estancias-coto-x-kg/_/A-00047985-00047985-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bife-angosto-estancias-coto-x-kg/_/A-00047987-00047987-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bife-parrilla-estancias-coto-x-kg/_/A-00048129-00048129-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bife-con-lomo-estancias-coto-x-kg/_/A-00047988-00047988-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapa-de-nalga-estancias-coto-x-kg/_/A-00048128-00048128-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-asado-del-medio-estancias-coto-x-kg/_/A-00047979-00047979-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-picanha-estancias-coto-x-kg/_/A-00043059-00043059-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-milanesa-bola-de-lomo-estancias-coto-x-kg/_/A-00047993-00047993-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-bondiola-de-cerdo-finas-hierbas-x-kg/_/A-00011943-00011943-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-vacio-del-centro-estancias-coto-x-kg/_/A-00047980-00047980-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-picada-desgrasada-estancias-coto-x-kg/_/A-00048124-00048124-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-colita-de-cuadril-estancias-coto-x-kg/_/A-00047990-00047990-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-peceto--estancias-coto-x-kg/_/A-00047994-00047994-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-molleja-x-kg/_/A-00000078-00000078-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-chinchulin-x-kg/_/A-00000028-00000028-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-entrana-x-kg/_/A-00041389-00041389-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-morcilla-e-v-criolla-bb-x-u-magret-paq-1-uni/_/A-00012340-00012340-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-chorizo-e-v-de-cerdo-x-un-magret-uni-1-uni/_/A-00012338-00012338-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-chorizo-fco-gancho-fridevi--1-kgm/_/A-00011644-00011644-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-chorizo-e-v-de-cerdo-cagnoli-uni-1-uni/_/A-00473454-00473454-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-chorizo-de-cerdo-coto-envasado-al-vacio-x-kg/_/A-00040763-00040763-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-morcilla-atada-paladini-xkg/_/A-00017380-00017380-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-longaniza-parrillera-de-cerdo-ciudad-del-lago-x-kg/_/A-00036507-00036507-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salchicha-parrillera-paladini-xkg/_/A-00017446-00017446-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-morcilla-rosca-paladini-xkg/_/A-00017445-00017445-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-chorizo-de-cerdo-bombon-ciudad-del-lago-x-kg/_/A-00036503-00036503-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-noquis-de-calabaza-bandeja/_/A-00013699-00013699-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-noquis-granel-huevo---1-kgm/_/A-00013570-00013570-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-noquis-papa-mendia-500-grm/_/A-00461048-00461048-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-fideos-finos-al-huevo-x-kg/_/A-00044643-00044643-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-fideos-a-la-crema-x-kg/_/A-00044224-00044224-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-fideos-caseros-al-pesto-x-kg/_/A-00006039-00006039-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-noquis--la-saltena-ban-900-grm/_/A-00500614-00500614-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-panzottis-de-verdura-y-jamon-cocido---2-planchas/_/A-00044263-00044263-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-ravioles-ricota-olivia---2-planchas/_/A-00044326-00044326-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-ravioles-verdura-y-queso---2-planchas/_/A-00044297-00044297-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-sorrentino-de-ricota-jamon-y-mozzarella---2-planchas/_/A-00044267-00044267-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-ravioles-ricota-mendia-bsa-1-kgm/_/A-00468762-00468762-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-ravioles-pasteuriz-pollo-y-verdur-mendia-bli-500-grm/_/A-00256086-00256086-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-ravioles-jamon-y-queso-yuli-bli-500-grm/_/A-00491165-00491165-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-sorrentino-de-panceta-y-verdeo---1-plancha/_/A-00012640-00012640-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-sorrentinos-cver-alb-muzz----bja-1-uni/_/A-00013144-00013144-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-raviol-jamon-y-queso-la-saltena-x-450-gr/_/A-00511289-00511289-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapa-p-pascualina-criolla-coto-fwp-400-grm/_/A-00290327-00290327-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapa-p-pascualina--coto-bol-400-grm/_/A-00026582-00026582-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapempanada-criolla-x20-mendia-bsa-520-grm/_/A-00258362-00258362-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapa-p-pascualina-hojaldre-punto&pasta-bsa-400-grm/_/A-00505531-00505531-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapa-p-pascualina-hojaldre-villa-dagri-fwp-400-grm/_/A-00475345-00475345-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapa-p-pascualina-integral-mendia-bsa-400-grm/_/A-00488394-00488394-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapempanada-x18-uni-hojald-signo-de-or-fwp-450-grm/_/A-00505626-00505626-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapempanada-criolla-mendia-bsa-390-grm/_/A-00191133-00191133-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapempanada-criolla-punto&pasta-bsa-300-grm/_/A-00505529-00505529-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapa-p-pascualina-criolla-mendia-bsa-400-grm/_/A-00191131-00191131-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapempanada-hojaldre-villa-dagri-fwp-300-grm/_/A-00475346-00475346-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapempanada-horno-mendia-bsa-390-grm/_/A-00191132-00191132-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapa-p-pascualina-hojaldre-vb-la-saltena-bsa-400-gr/_/A-00263843-00263843-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tapempanada-rotisera-criol-noly-paq-460-grm/_/A-00499136-00499136-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-panqueques-redondo-tuzzvill-bsa-200-grm/_/A-00067863-00067863-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salchichas-kids-x-6-uni-swift-kids-paq-190-grm/_/A-00491745-00491745-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salchicha-clasica-vienissima-paq-1-grm/_/A-00299037-00299037-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salchicha-escudo-de-oro-sin-piel-paq-6-uni-190-grm/_/A-00225560-00225560-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aceitunas-rellenas--xkg/_/A-00000736-00000736-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pickles-e-vinagre--xkg/_/A-00000859-00000859-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pollo-entero-fresco-x-uni-(3-kg)/_/A-00012785-00012785-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pollo-congelado-x-kg/_/A-00042989-00042989-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-vegano-cremoso-biorganic-x-500-grm/_/A-00533348-00533348-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-vegano-felices-las-vacas-cremoso-felices-500-gr/_/A-00509602-00509602-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-vegano-cheddar-en-fetas-felices-las-vacas-paq-200-grm/_/A-00533337-00533337-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-untable-port-salut-light-la-serenisima-pot-180-grm/_/A-00525549-00525549-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-untable-port-salut-light-la-serenisima-pot-180-grm/_/A-00525549-00525549-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-ahumado-la-suerte-x-kg/_/A-00012760-00012760-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-quesmuzzd-lat-bocconcino-wapi-pou-160-grm/_/A-00502096-00502096-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-brie--piedras-bla-paq-160-grm/_/A-00484191-00484191-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-camembert-finlandia-unidad-200gr/_/A-00011182-00011182-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-rallado-la-paulina-paq-150-grm/_/A-00014059-00014059-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-quesrallado--spalen-paq-120-grm/_/A-00134465-00134465-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-quesrallado--coto-paq-500-grm/_/A-00002749-00002749-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-rallado-ilolay-paq-115-grm/_/A-00532274-00532274-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-rallado-reggianito-la-serenisi-sob-130-grm/_/A-00510760-00510760-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-crema-original-la-serenisima-pot-290-grm/_/A-00528591-00528591-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-crema-la-paulina-tradicional-290-gr/_/A-00212429-00212429-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-blanco-clasico-garcia-pot-290-grm/_/A-00531712-00531712-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-crema-la-paulina-light-290-gr/_/A-00212430-00212430-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-untable-la-paulina-clasico-190-gr/_/A-00174397-00174397-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-crema-light-crematto-light-milkaut-pot-450-grm/_/A-00515111-00515111-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-untable-clasico-adler-pot-190-grm/_/A-00510420-00510420-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-untable-clasico-tonadita-pot-190-grm/_/A-00505160-00505160-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-blanco-light-ilolay-pot-290-grm/_/A-00532712-00532712-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-crema-light-casancrem-pot-480-grm/_/A-00530560-00530560-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-blanco-veronica-sin-sal-agregada-250-gr/_/A-00224959-00224959-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-untable-tregar-mascarpone-200-gr/_/A-00205420-00205420-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-queso-crema-la-paulina-doble-crema-250-gr/_/A-00213758-00213758-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pizzeta-mozza-x3-uni-pietro-540-grm/_/A-00538712-00538712-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pizza-mozzarella-1-2-sibarita-cja-665-grm/_/A-00231878-00231878-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pizza-xl-mozzarella-sibarita-cja-680-grm/_/A-00287956-00287956-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pizza-muz-jm-mo-sibarita-cja-570-grm/_/A-00066716-00066716-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pizza-pepperoni-pietro-cja-600-grm/_/A-00523516-00523516-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-croquetas-brocoli-gds-granja-del-bsa-400-grm/_/A-00265758-00265758-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-croquetas-papa-y-mozzare-granja-del-fwp-400-grm/_/A-00261436-00261436-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-medallones-vegetales-nutrileza---4-uni-x-90-gr-aduki-&-curcuma/_/A-00489550-00489550-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-medallones-burger-swift---4-uni-x-69-gr--/_/A-00166470-00166470-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-hamburguesa-carne-vacuna-x-paty-cja-288-grm/_/A-00510292-00510292-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-medallones-vegetales-vegetalex---4-uni-x-75-gr-legumbres-y-quinoa/_/A-00485582-00485582-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-hamburguesas-swift--12-uni-x-80-gr-clasicas/_/A-00290730-00290730-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-hamburguesas-paty--20-uni-x-80-gr-clasicas/_/A-00295047-00295047-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-milanesas-soja-x4-lucchetti-paq-560-grm/_/A-00515414-00515414-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-espinaca--granja-del-bsa-500-grm/_/A-00025342-00025342-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-papas-corte-tradicio-simplot-bsa-1100-grm/_/A-00485925-00485925-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-congelados-nuggets-patitas-y-bocaditos-nuggets/_/N-1azz6sk'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-nuggets-pollo-tres-arroyo-bsa-400-grm/_/A-00285892-00285892-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-nuggets-de-carne-swift-bsa-380-grm/_/A-00254469-00254469-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-papas-noisette-mc-cain-bsa-1-kgm/_/A-00035033-00035033-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-papel-higienico-campanita-soft-plus-xl-simple-hoja-paquete-4-unidades/_/A-00295882-00295882-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-papel-higienico-felpita-simple-hoja-paquete-4-unidades/_/A-00262405-00262405-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-papel-higienico-higienol-max-hoja-simple-panal-paq-4-unid-x-100-mts-c-u/_/A-00531082-00531082-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-phigienico-hoja-simple-x4-elite-paq-8-m2/_/A-00523556-00523556-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-fibra-esponja-virulana-multiuso-lisa-paq-1-uni/_/A-00199823-00199823-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-virulana-inoxy-x1-uni/_/A-00042855-00042855-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-esponja-3x2-scotch-brit-paq-3-uni/_/A-00298338-00298338-200'
        ,'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-esponjago!lisalimpiezafacil/_/A-00470487-00470487-200'

       ]

    fecha = datetime.strptime(date_dash.replace("'",""),"%Y-%m-%d").strftime('%-m-%-d-%Y')
    print("fecha de ejecucion: ", fecha)

    fecha_file = date_nodash
    print("archivo a generar: ", fecha_file)

    fecha_folder = datetime.strptime(date_dash.replace("'",""),"%Y-%m-%d").strftime('%Y%m')
    print("carpeta a crear: ",fecha_folder)

    print(f"Se procesaran {len(set(urls))} productos")
    
    new_df = pd.DataFrame(columns=['fecha','plu','nombre_producto','precio_dia','precio_regular','disponible'])

    for url in set(urls):     
        try:
            html_content = requests.get(url).text
            soup = BeautifulSoup(html_content, "html.parser")

            #Nombre y PLU
            name_html = soup.find('h1', {'class': 'product_page'})
            plu_html = soup.find('span', {'class': 'span_codigoplu'})
            product_name = name_html.text.replace('\n','').replace('\t','').replace('\r','').lower().strip().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
            product_plu = plu_html.text.strip()

            #Declaracion del producto
            #print('producto: ', product_name)
            #print('PLU: ', product_plu)

            #Check disponibilidad
            product_avl = soup.find('div', {'class': 'product_not_available'})

            if product_avl is None:

                #print('Producto disponible')

                disponible = 1

                #Precios
                #HTML del container del precio
                precios_html = soup.find('div', {'class': 'info_discount info_productPrice'})

                #Check tipo de oferta
                #Oferta contado
                oferta_contado_html = str(soup.find_all('div', {'class': 'ofertaContado'}))
                es_oferta_contado = 'OFERTA' in oferta_contado_html

                #print('es oferta contado: ', es_oferta_contado)
                if es_oferta_contado:
                    
                    #print("Producto con oferta de contado")

                    precio_regular_html = precios_html.find_next('div', {'class': 'product_discount_container'}).find('span', {'class': 'price_regular_precio'})
                    precio_regular = float(precio_regular_html.text.replace('$','').strip())
                    #print("Precio regular: ", precio_regular)

                    precio_descuento_html = precios_html.find_next('span', {'class': 'atg_store_productPrice'}).find('span', {'class': 'atg_store_newPrice'})
                    precio_descuento = float(str(precio_descuento_html).split('$')[1].split('\n')[0].replace('.','').replace(',','.'))
                    #print("Precio oferta: ", precio_descuento)

                else:
                    #Precio contado
                    precio_regular_html = precios_html.find_next('span', {'class': 'atg_store_newPrice'})
                    precio_regular = float(precio_regular_html.text.split('$')[1].strip().replace('.','').replace(',','.'))
                    #print('Precio regular: ', precio_regular)

                    #Precios con descuento
                    #Para chequear si el descuento es real o es algo viejo que quedo en el codigo
                    precios_descuento_html = precios_html.find_next('div', {'class': 'product_discount_container'})

                    try:
                        check_precio_regular = float(precios_descuento_html.find_next('span',{'class': 'price_regular_precio'}).text.replace('$','').strip().replace('.','').replace(',','.'))

                    except AttributeError:
                        try:
                            check_precio_regular = float(precios_descuento_html.find_next('span',{'class': 'atg_store_oldPrice price_regular'}).text.replace('$','').strip().replace('.','').replace(',','.'))
                        
                        except AttributeError:
                            check_precio_regular = None


                    ##print('Precio regular check: ', check_precio_regular)
                    ##print('Son iguales:', precio_regular == check_precio_regular)

                    if precio_regular == check_precio_regular:
                        precio_descuento = float(precios_descuento_html.find_next('span', {'class': 'price_discount'}).text.replace('$','').replace('c/u','').strip().replace(',','.'))

                    else:
                        precio_descuento = precio_regular

                    ##print('Precio regular: ', precio_regular)
                    ##print('Precio oferta: ', precio_descuento)

            else:
                #print("Producto no disponible - se tomara el precio solo como referencia")

                disponible = 0
                
                try:
                    price_regular_html = soup.find_all('span', class_="price_regular_precio")
                    price_html = soup.find_all('span', class_="atg_store_productPrice")

                    precio_descuento = float(str(price_html).split('$')[1].split('\n')[0].replace('.','').replace(',','.'))

                    if price_regular_html == []: #si hay oferta, usamos el precio regular, si no, el precio del dia es el precio regular
                        precio_regular = precio_descuento
                    else: 
                        precio_regular = float(price_regular_html[0].text.split('$')[1]).replace('.','')

                    precio_descuento = precio_regular
                    #print('Precio regular: ', precio_regular)
                    #print('Precio oferta: ', precio_descuento)           
                    
                except:
                    pass

            to_append = [fecha, product_plu, product_name, precio_descuento, precio_regular, disponible]
            row = pd.Series(to_append, index = new_df.columns)
            new_df = new_df.append(row, ignore_index = True)
        
        except:
            #print(f'No se encontro el producto {url}')
            pass

        
    
    print("Scrapping finalizado")        

    df_historia = pd.read_csv("/opt/airflow/dags/files/precios_coto.csv")
    df_historia.drop(df_historia[df_historia.fecha == fecha].index, inplace = True)

    df_historia = df_historia.append(new_df, ignore_index = True)
    df_historia.drop_duplicates(inplace = True)

    path = f"/opt/airflow/dags/files/{fecha_folder}"
    path_exists = os.path.exists(path)

    if not path_exists:
        os.makedirs(path)
    df_historia.to_csv(f"/opt/airflow/dags/files/{fecha_folder}/{env}precios_coto_{fecha_file}.csv", index = False)
    df_historia.to_csv(f"/opt/airflow/dags/files/{env}precios_coto.csv", index = False)

def calc_increment():

    #Levantamos el ultimo archivo actualizado al dia anterior
    df_historia = pd.read_csv(f"/opt/airflow/dags/files/{env}precios_coto.csv")   

    df_historia['fecha'] = pd.to_datetime(df_historia['fecha'], format = '%m-%d-%Y')

    df_final = pd.DataFrame(columns = ['fecha','plu','nombre_producto','precio_dia','precio_regular','disponible','incremento_diario','incremento_semanal'])

    for producto in df_historia.nombre_producto.unique():
        df_incremento = df_historia[df_historia['nombre_producto'] == producto].sort_values(by='fecha', ascending=True)
        #incrementos = [((df_incremento[i:i+1].precio.values / df_incremento[i-1:i].precio.values)[0]-1)*100 for i in range(1,len(df_incremento))]
        df_incremento['incremento_diario'] = round(df_incremento.precio_regular.pct_change(periods=1)*100,2)
        df_incremento['incremento_semanal'] = round(df_incremento.precio_regular.pct_change(periods=7)*100,2)
        
        df_final = df_final.append(df_incremento, ignore_index = True)

    df_final.drop_duplicates(inplace = True)
    df_final = df_final.sort_values(by=['fecha','incremento_semanal'], ascending=False)

    df_final.to_csv(f"/opt/airflow/dags/files/{env}precios_coto_increm.csv", index = False)
