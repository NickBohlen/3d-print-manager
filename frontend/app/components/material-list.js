import Component from '@glimmer/component';
import { inject as service } from '@ember/service';
import { tracked } from '@glimmer/tracking';

export default class MaterialListComponent extends Component {
    @service materialsApi;

    @tracked materials = [];

    constructor() {
        super(...arguments);
        console.log('MaterialList Component initialized');
        this.loadMaterials();
    }

    async loadMaterials() {
        console.log('Loading materials...');
        await this.materialsApi.fetchMaterials();
        console.log('Materials fetched:', this.materialsApi.materials);
        this.materials = this.materialsApi.materials;
        console.log('Materials assigned to this.materials:', this.materials);
    }
}