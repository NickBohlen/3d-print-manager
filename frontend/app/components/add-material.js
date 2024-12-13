import Component from '@glimmer/component';
import { tracked } from '@glimmer/tracking';
import { action } from '@ember/object';
import { inject as service } from '@ember/service';

export default class AddMaterialComponent extends Component {
    @service materialsApi;

    @tracked name = '';
    @tracked type = 'PLA';
    @tracked color = '';
    @tracked initialQuantity = 0;
    @tracked reorderThreshold = 0;

    @action
    updateName(event) {
        this.name = event.target.value;
    }

    @action
    updateType(event) {
        this.type = event.target.value;
    }

    @action
    updateColor(event) {
        this.color = event.target.value;
    }

    @action
    updateInitialQuantity(event) {
        this.initialQuantity = event.target.value;
    }

    @action
    updateReorderThreshold(event) {
        this.reorderThreshold = event.target.value;
    }

    @action
    async addMaterial(event) {
        event.preventDefault();
        await this.materialsApi.addMaterial({
            name: this.name,
            type: this.type,
            color: this.color,
            initial_quantity: this.initialQuantity,
            reorder_threshold: this.reorderThreshold,
            current_quantity: this.initialQuantity
        });
        this.name = '';
        this.type = 'PLA';
        this.color = '';
        this.initialQuantity = 0;
        this.reorderThreshold = 0;
    }
}
