(function() {
    window.onload = function() {
        function getImages() {
            // Return an object containing image URLs and widths for all regions
            var descendants, i, images;

            images = {};
            for (name in editor.regions) {
                // Search each region for images
                descendants = editor.regions[name].descendants();
                for (i = 0; i < descendants.length; i++) {
                    // Filter out elements that are not images
                    if (descendants[i].constructor.name !== 'Image') {
                        continue;
                    }
                    images[descendants[i].attr('src')] = descendants[i].size()[0];
                }
            }

            return images;
        }

        var FIXTURE_TOOLS, editor, req;

        ContentTools.IMAGE_UPLOADER = ImageUploader.createImageUploader;
        editor = ContentTools.EditorApp.get();

        editor.init('[data-editable], [data-fixture]', 'data-name');

        editor.addEventListener('saved', function(ev) {
            var name, onStateChange, passive, payload, regions, xhr;

            // Check if this was a passive save
            passive = ev.detail().passive;

            // Check to see if there are any changes to save
            regions = ev.detail().regions;
            if (Object.keys(regions).length == 0) {
                return;
            }

            // Set the editors state to busy while we save our changes
            this.busy(true);

            // Collect the contents of each region into a FormData instance
            payload = new FormData();
            payload.append('page', window.location.pathname);
		    payload.append('images', JSON.stringify(getImages()));
            for (name in regions) {
                payload.append(name, regions[name]);
            }

            // Send the update content to the server to be saved
            onStateChange = function(ev) {
                // Check if the request is finished
                if (ev.target.readyState == 4) {
                    editor.busy(false);
                    if (ev.target.status == '200') {
                        // Save was successful, notify the user with a flash
                        if (!passive) {
                            new ContentTools.FlashUI('ok');
                        }
                    } else {
                        // Save failed, notify the user with a flash
                        new ContentTools.FlashUI('no');
                    }
                }
            };

            element = document.querySelector('meta[name="page-id"]');
		    page_id = element.getAttribute('content')

            API.call('put', '/api/v1/post/'+page_id+'/', payload, true, onStateChange)
        });

        // Add support for auto-save
        editor.addEventListener('start', function (ev) {
            var _this = this;

            // Call save every 30 seconds
            function autoSave() {
                _this.save(true);
            };
            this.autoSaveTimer = setInterval(autoSave, 30 * 1000);
        });

        editor.addEventListener('stop', function (ev) {
            // Stop the autosave
            clearInterval(this.autoSaveTimer);
        });

        FIXTURE_TOOLS = [['undo', 'redo', 'remove']];

        ContentEdit.Root.get().bind('focus', function(element) {
            var tools;
            if (element.isFixed()) {
                tools = FIXTURE_TOOLS;
            } else {
                tools = ContentTools.DEFAULT_TOOLS;
            }
            if (editor.toolbox().tools() !== tools) {
                return editor.toolbox().tools(tools);
            }
        });

        // Русский перевод подгруим же
        req = new XMLHttpRequest();
        req.overrideMimeType('application/json');
        req.open('GET', 'https://raw.githubusercontent.com/GetmeUK/ContentTools/master/translations/ru.json', true);

        function onStateChange (ev) {
            var translations;
            if (ev.target.readyState == 4) {
                translations = JSON.parse(ev.target.responseText);
                ContentEdit.addTranslations('ru', translations);
                ContentEdit.LANGUAGE = 'ru';
            }
        };
        req.addEventListener('readystatechange', onStateChange);
        req.send(null);
    };

}).call(this);
