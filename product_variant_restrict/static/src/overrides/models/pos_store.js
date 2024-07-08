/** @odoo-module */
import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";

patch(PosStore.prototype, {
    
    _loadProductProduct(products) {  
        
        var given_config = new RegExp('[\?&]config_id=([^&#]*)').exec(window.location.href);
        this.config_id = given_config && given_config[1] && parseInt(given_config[1]) || false;

        var indexArray = [];

        // Find indexes of elements to be removed
        for (var i = 0; i < products.length; i++) {
        if (products[i]['bey_pass_counter_ids'].includes(this.config_id)) {
            indexArray.push(i);
        }
        }

        // Remove elements using splice
        for (var j = indexArray.length - 1; j >= 0; j--) {
        products.splice(indexArray[j], 1);
        }

        super._loadProductProduct(...arguments);
    },

});
