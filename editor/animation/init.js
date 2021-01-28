//Dont change it
//Dont change it
requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {
        
        var $tryit;

        var io = new extIO({
            multipleArguments: true,
            functions: {
                python: 'sum_light',
                js: 'sumLight'
            }
        });
        io.parseInputArguments = function(data) {
            var fname = '';
            var is_py = this.getLanguage() == "python"
            if (is_py) {
                fname = 'datetime';
            } else {
                fname = 'new Date';
            }
            var els = data[0];
            els = els.map(function(ee) {
                if (ee.length === 2) {
                    return '[' + fname + '(' + ee[0].join(', ') + '), ' + ee[1] + ']'
                } else {
                    return fname + '(' + ee.join(', ') + ')'    
                }
                
            })
            els = '[\n' + els.join(',\n') + '\n]'
            if (is_py) {
                els = 'els=' + els;
            }

            var start_watching = '';
            var end_watching = '';
            var operating = '';
            var req = '';

            if (is_py) {
                if (data.length > 1 && data[1]) {
                    start_watching = ',\nstart_watching=' + fname + '(' + data[1].join(', ') +')';
                }
                if (data.length > 2 && data[2]) {
                    end_watching = ',\nend_watching=' + fname + '(' + data[2].join(', ') +')';
                }
                if (data.length > 3 && data[3]) {
                    operating = ',\noperating=timedelta(seconds=' + data[3] +')';
                }
                if (data.length > 4 && data[4]) {
                    req = ',\nreq=' + data[4];
                }
            } else {
                if (data.length > 1) {
                    if (data[1]){
                        start_watching = ',\n' + fname + '(' + data[1].join(', ') +')';
                    } else {
                        start_watching = ',\n' + data[1];
                    }
                }
                if (data.length > 2) {
                    if (data[2]){
                        end_watching = ',\n' + fname + '(' + data[2].join(', ') +')';
                    } else {
                        end_watching = ',\n' + data[2];
                    }
                }
                if (data.length > 3) {
                    operating = ',\n' + data[3];
                }
                if (data.length > 4) {
                    req = ',\n' + data[4];
                }
            }

            

            return els + start_watching + end_watching + operating;
        }
        io.start();
    }
);
