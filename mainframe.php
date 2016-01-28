
<div style="width:100%;">
    <table>
        <tr>
            <td>
                <div class="bigblock">
                    <div class="subtitle"> <b>C</b>omprehensive <b>R</b>edundancy <b>A</b>nalysis for Complete <b>P</b>roteomes </div>

                    <div class="general">
                        <form name="download" action="results.php" method="POST" enctype="multipart/form-data">
                            <div id="download_area">
                                <br><b>FASTA: </b> <input type="file" name="fastaseq"><p>
                                <b>EMAIL: </b> <input type="text" name="email"></input>
                                <p><b>PARAMETERS</b></p>
                                <table>
                                    <tr>
                                        <td>CD-HIT Threshold:</td>
                                        <td><input type="text" name="ct" value="0.7"></input></td>
                                    </tr>
                                    <tr>
                                        <td>CD-HIT Fractional Length:</td>
                                        <td><input type="text" name="cl" value="0.8"></input></td>
                                    </tr>
                                    <tr>
                                        <td>0j Minimum Complexity: </td>
                                        <td><input type="text" name="zj" value="0.9"></input></td>
                                    </tr>
                                    <tr>
                                        <td>Minimum Length: </td>
                                        <td><input type="text" name="min" value="30"></input></td>
                                    </tr>
                                    <tr>
                                        <td>Maximum Length: </td>
                                        <td><input type="text" name="max" value="30000"></input></td>
                                    </tr>
                                    <tr>
                                        <td>Maximum Number of "X"s to be ignored:</td>
                                        <td><input type="text" name="xs" value="0"></input></td>
                                    </tr>
                                    <tr>
                                        <td>Fusion/Fission Threshold:</td>
                                        <td><input type="text" name="fft" value="0.7"></input></td>
                                    </tr>
                                    <tr>
                                        <td>Fusion/Fission Fractional Length:</td>
                                        <td><input type="text" name="ffl" value="0.8"></input></td>
                                    </tr>
                                </table>
                                <input type="checkbox" name="ms"> Check for M at beginning of sequence? <br>
                                <input type="checkbox" name="dlen"> Destage Length Filter? <br>
                                <input type="checkbox" name="dcomp"> Destage Complexity (0j) Filter? <br>
                                <input type="checkbox" name="dred"> Destage Redundancy (CD-HIT) Filter? <br>
                                <input type="checkbox" name="dff"> Destage Fusion/Fission (Ff) Filter? <br>
                                <p></p>
                                <input type="submit"/>
                            </div>
<p>
                    <a href="index.php"><div class="headline">C.R.A.P. web server</div> <p> </a>
                        </form>
                    </div>
                </div>
            </td>
    </table>
</div>